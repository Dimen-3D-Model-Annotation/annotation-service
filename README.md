## Dimen
#### A collaborative 3D model annotation tool

### Annotation Service

1. `cd backend-services`
2. `git clone https://github.com/Dimen-3D-Model-Annotation/annotation-service.git`
3. `cd annotation-service`
4. `py -3 -m venv venv`

5. view -> Command Palette -> Python:Select Interpreter -> Enter interpreter path -> Find -> Select Interpreter
`.\annotation-service\venv\Scripts\python.exe`

6. `venv\Scripts\activate.bat`

7. `pip install -r requirements.txt`

8. To run the FastAPI app
    `uvicorn app.main:app --reload`
   If you want to run on another port other than default port 8000
    `uvicorn app.main:app --reload --host 0.0.0.0 --port 8001`
