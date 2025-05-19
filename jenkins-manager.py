#!/usr/bin/env python3
"""
Skrypt do zarządzania zadaniami Jenkins przez API.
Umożliwia listowanie zadań, sprawdzanie statusu i uruchamianie buildów.
"""

import requests
import sys
import json
import argparse
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin


class JenkinsAPI:
    def __init__(self, base_url, username=None, api_token=None):
        """
        Inicjalizacja klienta Jenkins API.
        
        Args:
            base_url (str): URL serwera Jenkins (np. http://jenkins.example.com/)
            username (str): Nazwa użytkownika Jenkins
            api_token (str): Token API użytkownika
        """
        self.base_url = base_url.rstrip('/') + '/'
        self.auth = None
        if username and api_token:
            self.auth = HTTPBasicAuth(username, api_token)
        self.headers = {'Content-Type': 'application/json'}

    def _make_request(self, method, endpoint, **kwargs):
        """
        Wykonuje żądanie HTTP do API Jenkins.
        
        Args:
            method (str): Metoda HTTP (GET, POST, itp.)
            endpoint (str): Ścieżka API
            **kwargs: Dodatkowe argumenty dla requests
            
        Returns:
            dict: Odpowiedź z API jako słownik
            
        Raises:
            Exception: W przypadku błędu połączenia lub odpowiedzi
        """
        url = urljoin(self.base_url, endpoint)
        
        try:
            response = requests.request(
                method,
                url,
                auth=self.auth,
                headers=self.headers,
                **kwargs
            )
            
            response.raise_for_status()
            
            if not response.content:
                return {}
                
            if 'json' in response.headers.get('Content-Type', ''):
                return response.json()
            
            return {'status': 'success', 'message': response.text}
            
        except requests.exceptions.HTTPError as e:
            print(f"Błąd HTTP: {e}")
            if hasattr(e, 'response') and e.response:
                print(f"Treść odpowiedzi: {e.response.text}")
            sys.exit(1)
        except requests.exceptions.ConnectionError:
            print("Błąd połączenia z serwerem Jenkins")
            sys.exit(1)
        except requests.exceptions.Timeout:
            print("Timeout podczas łączenia z serwerem Jenkins")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            print(f"Błąd żądania: {e}")
            sys.exit(1)
        except json.JSONDecodeError:
            print("Błąd parsowania odpowiedzi JSON")
            sys.exit(1)

    def list_jobs(self):
        """
        Pobiera listę wszystkich zadań z Jenkins.
        
        Returns:
            list: Lista zadań
        """
        response = self._make_request('GET', 'api/json?tree=jobs[name,url,color]')
        return response.get('jobs', [])

    def get_job_info(self, job_name):
        """
        Pobiera szczegółowe informacje o zadaniu.
        
        Args:
            job_name (str): Nazwa zadania
            
        Returns:
            dict: Szczegóły zadania
        """
        endpoint = f'job/{job_name}/api/json'
        return self._make_request('GET', endpoint)

    def get_build_status(self, job_name, build_number='lastBuild'):
        """
        Pobiera status konkretnego buildu.
        
        Args:
            job_name (str): Nazwa zadania
            build_number (str/int): Numer buildu lub 'lastBuild'
            
        Returns:
            dict: Status buildu
        """
        endpoint = f'job/{job_name}/{build_number}/api/json'
        return self._make_request('GET', endpoint)

    def build_job(self, job_name, parameters=None):
        """
        Uruchamia zadanie w Jenkins.
        
        Args:
            job_name (str): Nazwa zadania
            parameters (dict): Parametry do przekazania (opcjonalnie)
            
        Returns:
            dict: Wynik operacji
        """
        if parameters:
            endpoint = f'job/{job_name}/buildWithParameters'
            return self._make_request('POST', endpoint, params=parameters)
        else:
            endpoint = f'job/{job_name}/build'
            # Dodajemy token CSRF jeśli jest wymagany
            crumb = self._get_crumb()
            headers = self.headers.copy()
            if crumb:
                headers.update(crumb)
            return self._make_request('POST', endpoint, headers=headers)

    def _get_crumb(self):
        """
        Pobiera token CSRF jeśli ochrona CSRF jest włączona.
        
        Returns:
            dict: Nagłówek z tokenem CSRF lub None
        """
        try:
            response = self._make_request('GET', 'crumbIssuer/api/json')
            return {response.get('crumbRequestField'): response.get('crumb')}
        except Exception:
            return None


def main():
    parser = argparse.ArgumentParser(description='Jenkins API Client')
    parser.add_argument('--url', required=True, help='Jenkins URL')
    parser.add_argument('--username', help='Jenkins username')
    parser.add_argument('--token', help='Jenkins API token')
    
    subparsers = parser.add_subparsers(dest='command', help='Command')
    
    # Komenda list
    subparsers.add_parser('list', help='List all Jenkins jobs')
    
    # Komenda status
    status_parser = subparsers.add_parser('status', help='Check job build status')
    status_parser.add_argument('job_name', help='Name of the job')
    status_parser.add_argument('--build', default='lastBuild', help='Build number (default: lastBuild)')
    
    # Komenda build
    build_parser = subparsers.add_parser('build', help='Trigger a job build')
    build_parser.add_argument('job_name', help='Name of the job to build')
    build_parser.add_argument('--param', action='append', nargs=2, metavar=('KEY', 'VALUE'), 
                             help='Build parameters (can be used multiple times)')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Inicjalizacja klienta API
    jenkins = JenkinsAPI(args.url, args.username, args.token)
    
    # Wykonanie odpowiedniej komendy
    if args.command == 'list':
        jobs = jenkins.list_jobs()
        print(f"Znaleziono {len(jobs)} zadań:")
        for job in jobs:
            status = "aktywne" if job.get('color') != 'disabled' else "wyłączone"
            print(f"- {job.get('name')} ({status})")
    
    elif args.command == 'status':
        try:
            build_info = jenkins.get_build_status(args.job_name, args.build)
            print(f"Status zadania '{args.job_name}' (build #{build_info.get('number', 'unknown')}):")
            print(f"- Wynik: {build_info.get('result', 'w trakcie')}")
            print(f"- Czas rozpoczęcia: {build_info.get('timestamp', 'nieznany')}")
            print(f"- Czas trwania: {build_info.get('duration', 0)/1000:.2f} sekund")
            print(f"- URL: {build_info.get('url', 'nieznany')}")
        except Exception as e:
            print(f"Nie można pobrać informacji o buildzie: {e}")
    
    elif args.command == 'build':
        parameters = {}
        if args.param:
            for key, value in args.param:
                parameters[key] = value
        
        try:
            result = jenkins.build_job(args.job_name, parameters if parameters else None)
            print(f"Zadanie '{args.job_name}' zostało uruchomione")
            if 'location' in result:
                print(f"URL do śledzenia: {result['location']}")
        except Exception as e:
            print(f"Nie można uruchomić zadania: {e}")


if __name__ == "__main__":
    main()
