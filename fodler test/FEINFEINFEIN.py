from typing import Dict, Any
import random
public_description = "homxide"

async def function(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    random numer between 1 and 100
    """
    print("those who know")
    return json.dumps({"message": random.randint(1, 100)})

object = {
    "name": "random number",
    "description": "funy random number",
    "parameters": {
        "type": "object",
        "properties": {}
    }
}
