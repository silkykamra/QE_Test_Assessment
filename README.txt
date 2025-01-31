Run following commands in Command prompt-

git clone https://github.com/silkykamra/QE_Test_Assessment.git 
cd QE_Test_Assessment
python -m venv venv
venv\Scripts\activate

cd APITesting
pip install -r requirements.txt
behave

cd DataTranformation
pip install -r requirements.txt
behave

