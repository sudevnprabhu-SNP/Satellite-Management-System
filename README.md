    # Satellite Management System

    A menu-driven, space-themed Python program for managing spacecraft records in memory.

    ## Features

    - Add satellite records with generated IDs
- View and sort satellite records; filter records by supported fields
- Search by satellite ID and selected record fields
- Update satellite information and change operational status
- Refuel and consume fuel with range checks
- Delete records with confirmation details
- Display summary statistics and warnings for low fuel or older satellites

    ## Requirements

    Uses only the Python standard library; no third-party packages are required.

    - Recommended Python version: Python 3.10 or newer.
    - See [`requirements.txt`](requirements.txt).

    ## Run locally

    1. Install Python 3.
    2. Clone this repository or download it as a ZIP.
    3. Open a terminal in the repository root.
    4. Run:

       ```bash
       python3 src/Satellite_Management.py
       ```

    ## Sample usage

    Start the program, choose an action from the menu, and follow the prompts. A sample record for Cartosat-3 is included.

    ## Project structure

    ```text
    Satellite-Management-System/
    ├── src/
    │   └── Satellite_Management.py
    ├── docs/
    │   └── screenshots/
    ├── README.md
    ├── requirements.txt
    └── LICENSE
    ```

    ## Screenshots

    Add terminal screenshots here after running the program. Suggested screenshots: main menu, satellite listing, search result, and statistics. No screenshots are included because none were provided.

    ## Data and persistence

    The program starts with sample records defined in the source code. Records are maintained in memory during the current run; they are not saved to a database or file.

    ## Limitations

    - Records are stored in a Python dictionary in memory; changes are lost when the program exits.
- This is a learning project, not an operational satellite-control or mission-planning system.
- Validation rules are simplified and should not be treated as authoritative satellite data.
- The program uses an interactive terminal menu; there is no GUI, database, or external API integration.

    ## License

    This project is distributed under the MIT License. See [`LICENSE`](LICENSE). The license applies to the original project code and documentation authored for this repository; any third-party materials retain their own terms.
