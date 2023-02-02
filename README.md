# Web based classic cryptography

## Members

| Name                           |   NIM    |
| ------------------------------ | :------: |
| Muhammad Garebaldhie ER Rahman | 13520029 |
| Frederik Imanuel Louis         | 13520163 |

## Tech Stack Used

### FE

- Node
- NextJS
- TypeScript
- SCSS

### BE

- Python
- Flask

## How To Run

First thing first its to install all the dependency listed in the tech stack section

### Backend

1. Install virtual environment `pip3 -m install virtualenv`
2. Create virual enviroment for your python `virtualenv venv`
3. Activate your virtual environment
   1. UNIX based: `source ./venv/bin/activate`
   2. Windows: `./venv/Scripts/activate`
4. Install the python dependency `pip3 -r install requirements.txt`
5. Run the service using `python app.py` or use `flask run -p 8000`

### Frontend

1. Make sure you have NodeJS in your computer
2. Install the dependencies `yarn install`
3. Run service `yarn dev`

## Available Cipher

- Vigenere Cipher
- Auto Key Vigenere Cipher
- Extended Vignere Cipher
- Playfair Cipher
- Hill Cipher
- Affine Cipher

## Folder Structure

Backend

```txt
.
├── app.py
├── encryption
│   ├── affine.py
│   ├── hill.py
│   ├── __init__.py
│   ├── playfair.py
│   ├── sanitize.py
│   └── vignere.py
├── requirements.txt
└── static
```

Frontend

```
.
├── next.config.js
├── next-env.d.ts
├── package.json
├── package-lock.json
├── public
│   ├── favicon.ico
│   ├── next.svg
│   ├── thirteen.svg
│   └── vercel.svg
├── README.md
├── src
│   ├── app
│   │   ├── (cipher)
│   │   │   ├── affine-cipher
│   │   │   │   ├── head.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── auto-key-vigenere-cipher
│   │   │   │   ├── head.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── basic.tsx
│   │   │   ├── extended-vigenere-cipher
│   │   │   │   ├── head.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── hill-cipher
│   │   │   │   ├── head.tsx
│   │   │   │   └── page.tsx
│   │   │   ├── layout.tsx
│   │   │   ├── not-found.tsx
│   │   │   ├── playfair-cipher
│   │   │   │   ├── head.tsx
│   │   │   │   └── page.tsx
│   │   │   └── vigenere-cipher
│   │   │       ├── head.tsx
│   │   │       └── page.tsx
│   │   ├── (component)
│   │   │   ├── button-group.tsx
│   │   │   ├── cipher-list.tsx
│   │   │   └── key.tsx
│   │   ├── global-error.tsx
│   │   ├── globals.css
│   │   ├── head.tsx
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── styles
│   │   ├── Cipher.module.scss
│   │   ├── _mixins.scss
│   │   └── Root.module.scss
│   └── utils
│       ├── desc.ts
│       ├── fonts.ts
│       └── type.ts
├── tsconfig.json
├── yarn-error.log
└── yarn.lock
```
