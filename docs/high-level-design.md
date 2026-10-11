
flowchart TB
    USER["Engineer / User"]
    UI["Angular Dashboard<br/>Incidents · Timeline · Approval"]
    API["TRACE Backend — FastAPI<br/>Incident APIs · Validation · Auth"]

    USER --> UI --> API

    subgraph CORE["1 · AI INVESTIGATION ENGINE — LangGraph"]
        direction TB
        INTAKE["Incident Understanding"]
        HYP["Hypothesis Generator"]
        PLAN["Diagnostic Planner"]
        EXEC["Tool Selection & Execution"]
        EVID["Evidence Collector"]
        DECIDE{"Enough evidence?"}
        RCA["Root-Cause Report<br/>Evidence · Uncertainty · Recommendation"]
        INTAKE --> HYP --> PLAN --> EXEC --> EVID --> DECIDE
        DECIDE -->|"No — investigate further"| PLAN
        DECIDE -->|"Yes / limit reached"| RCA
    end

    API --> INTAKE

    subgraph TOOLS["2 · DIAGNOSTIC TOOL LAYER"]
        direction LR
        DEVICE["Device Status"]
        FIRMWARE["Firmware Checks"]
        CONFIG["Configuration"]
        LOGS["Logs / API Health"]
        NETWORK["Connectivity"]
        RETRIEVE["Knowledge Search"]
    end

    EXEC <--> TOOLS

    subgraph ENV["3 · SIMULATED ENTERPRISE ENVIRONMENT"]
        direction LR
        DS["Device Simulator"]
        FS["Firmware Service"]
        CS["Configuration Service"]
        LS["Log / API Service"]
        FI["Failure Injection Engine"]
    end

    TOOLS <--> ENV

    subgraph DATA["4 · DATA & KNOWLEDGE"]
        direction LR
        DB[("PostgreSQL<br/>Incidents · Devices · Evidence")]
        KB[("RAG Knowledge Base<br/>Manuals · Known Issues · History")]
        STATE[("Investigation State<br/>Checkpoints")]
    end

    ENV <--> DB
    RETRIEVE <--> KB
    CORE <--> STATE

    subgraph ACTION["5 · CONTROLLED REMEDIATION"]
        direction TB
        APPROVE{"Human Approval"}
        FIX["Validated Remediation Tool"]
        VERIFY["Verify System State"]
        RESULT["Final Incident Report"]
        APPROVE -->|"Approved"| FIX --> VERIFY --> RESULT
        APPROVE -->|"Rejected"| RESULT
    end

    RCA --> APPROVE
    FIX --> ENV
    VERIFY --> TOOLS
    RESULT --> API

    subgraph QUALITY["6 · TESTING & OBSERVABILITY"]
        direction LR
        EVAL["Evaluation Harness<br/>Ground Truth · Accuracy · Cost"]
        TEST["Pytest · Integration Tests"]
        TRACE["Logs · Agent Traces · Metrics"]
    end

    FI -.-> EVAL
    EVAL -.-> CORE
    TEST -.-> ENV
    CORE -.-> TRACE

    classDef interface fill:#dbeafe,stroke:#2563eb,color:#172554
    classDef agent fill:#ede9fe,stroke:#7c3aed,color:#3b0764
    classDef system fill:#dcfce7,stroke:#16a34a,color:#14532d
    classDef control fill:#ffedd5,stroke:#ea580c,color:#7c2d12
    classDef quality fill:#f1f5f9,stroke:#64748b,color:#0f172a

    class USER,UI,API interface
    class INTAKE,HYP,PLAN,EXEC,EVID,DECIDE,RCA agent
    class DEVICE,FIRMWARE,CONFIG,LOGS,NETWORK,RETRIEVE,DS,FS,CS,LS,FI,DB,KB,STATE system
    class APPROVE,FIX,VERIFY,RESULT control
    class EVAL,TEST,TRACE quality
