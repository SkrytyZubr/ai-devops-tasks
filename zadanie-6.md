graph LR
    A[Commit] --> B[Build]
    B --> C[Test]
    C --> D[Deploy]
    
    style A fill:#90CAF9,stroke:#1565C0
    style B fill:#A5D6A7,stroke:#2E7D32
    style C fill:#FFF59D,stroke:#F9A825
    style D fill:#EF9A9A,stroke:#C62828