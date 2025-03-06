

from fastapi import Request, Response
from starlette.background import BackgroundTask

from app.core.logging_config import log_request_info


async def logging_middleware(request: Request, call_next):
    req_body = await request.body()
    req_method = request.method
    req_path = request.url.path
    
    # Pass the request to the next handler
    response = await call_next(request)
    
    # Extract response body
    chunks = []
    async for chunk in response.body_iterator:
        chunks.append(chunk)
    res_body = b''.join(chunks)
    
    # Log the request and response in the background
    task = BackgroundTask(log_request_info, req_method, req_path, response.status_code, req_body.decode(), res_body.decode())
    
    # Return the response with a background task to log
    return Response(content=res_body, status_code=response.status_code,
                    headers=dict(response.headers), media_type=response.media_type, background=task)
    