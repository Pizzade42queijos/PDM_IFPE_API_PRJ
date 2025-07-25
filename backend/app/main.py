from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]  # em prod, substitua pelo domínio da API

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)