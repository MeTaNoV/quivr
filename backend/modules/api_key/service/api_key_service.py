from datetime import datetime, timedelta

from fastapi import HTTPException
from logger import get_logger
from modules.api_key.repository.api_key_interface import ApiKeysInterface
from modules.api_key.repository.api_keys import ApiKeys
from modules.user.entity.user_identity import UserIdentity
from modules.user.service.user_service import UserService
from pydantic import DateError

logger = get_logger(__name__)


user_service = UserService()


class ApiKeyService:
    repository: ApiKeysInterface

    def __init__(self):
        self.repository = ApiKeys()

    async def verify_api_key(
        self,
        api_key: str,
        only_chat: bool,
    ) -> bool:
        try:
            # Use UTC time to avoid timezone issues
            current_date = datetime.utcnow().date()
            result = self.repository.get_active_api_key(api_key)

            if result.data is not None and len(result.data) > 0:
                # TODO(pg): take into account only_chat parameter

                api_key_creation_date = datetime.strptime(
                    result.data[0]["creation_time"], "%Y-%m-%dT%H:%M:%S"
                ).date()

                api_key_expiration_date = api_key_creation_date + timedelta(
                    days=result.data[0]["days"]
                )

                if current_date <= api_key_expiration_date:
                    return True
            return False
        except DateError:
            return False

    async def get_user_from_api_key(
        self,
        api_key: str,
    ) -> UserIdentity:
        user_id_data = self.repository.get_user_id_by_api_key(api_key)

        if not user_id_data.data:
            raise HTTPException(status_code=400, detail="Invalid API key.")

        user_id = user_id_data.data[0]["user_id"]

        # TODO: directly UserService instead
        email = user_service.get_user_email_by_user_id(user_id)

        if email is None:
            raise HTTPException(status_code=400, detail="Invalid API key.")

        return UserIdentity(email=email, id=user_id)
