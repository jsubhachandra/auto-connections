# Daily automation


### Local setup

1. Fork the project
2. Clone the project to your machine
    ```
    git clone https://github.com/<your_username>/auto-connections.git
    ```
3. Create a virtual environment
    ```
    virtualenv env
    ```
4. Activate the virtual environment
    
    - Linux:
    `$ source venv/bin/activate`
    - Windows:
    `venv\Scripts\activate`
5. Install dependencies
    ```
    pip install -r requirements.txt
    ```
6. Create a directory named `bin` at the same level as `main.py`
7. [Download Chromedriver](https://chromedriver.chromium.org/downloads) and extract  to the bin directory above
8. Create a `.env` file in the root directory with following information:
    ```
    DEBUG=True
    LINKEDIN_USERNAME=<Your Linkedin Username>
    LINKEDIN_PASSWORD=<Your Linkedin_username>
    CHROMEDRIVER_PATH=<Path to Chromedriver>
    ```
9. Execute the script using `python main.py`