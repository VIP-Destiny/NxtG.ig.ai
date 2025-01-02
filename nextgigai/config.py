"""Application configuration."""

from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator

class Settings(BaseSettings):
    """Application settings."""

    PROJECT_NAME: str = "NextGigAI"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    # BACKEND_CORS_ORIGINS is a comma-separated list of origins
    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "nextgigai"
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        """Assemble database connection string."""
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    # JWT
    SECRET_KEY: str = "your-secret-key"  # TODO: Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # AI Models
    HERMES_API_URL: str = "http://localhost:8080"
    HERMES_API_KEY: Optional[str] = None

    class Config:
        """Pydantic config."""

        case_sensitive = True
        env_file = ".env"

settings = Settings()
