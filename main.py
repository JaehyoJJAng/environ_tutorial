from pathlib import Path
import os
import environ

def get_secret(base_dir:str)-> environ:
    env : environ.Environ = environ.Env(DEBUG=(bool,True))
    environ.Env.read_env(os.path.join(base_dir,r'.env\key.env'))
    return env

def main()-> None:
    # BASE DIR Setting
    BASE_DIR : str = Path(__file__).resolve().parent
    
    # Get Secret
    env : environ.Environ = get_secret(base_dir=BASE_DIR)
        
    cusmer_key    : str = env('test_cusmer_key')
    access_token  : str = env('test_access_token')    
    access_secret : str = env('test_access_secret')
    print(cusmer_key)
    print(access_secret)
    print(access_token)
    
if __name__ == '__main__':
    main()
