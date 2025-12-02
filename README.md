# Ad_generator

## To clone and use the code
```commandline
  git clone https://github.com/akilan97272/AD-idea-generator.git
  cd AD-idea-generator
```

## Package installation

### In conda...
```commandline
  conda create --name ad_generator
  conda activate ad_creator
  conda install pip # ignore if using anaconda
  pip install -r requriements.txt
```

### In normal python... 

```commandline
    python -m venv ad_generator
    source ad_generator/bin/activate
    pip install -r requriements.txt
```

## After package installation 

### To run the page in localhost

```commandline
    uvicorn main:app --reload
```

### To make it available in you network(only inside your subnet)
```commandline
    uvicorn main:app --host 0.0.0.0 --port 800
```

`currently style.css is empty. if needed you can add your custom styles`