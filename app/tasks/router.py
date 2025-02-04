from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.dependency import get_task_logic, get_task_service, get_request_user_id
from app.exceptions import TaskNotFoundException
from app.tasks.logic import TaskLogic
from app.tasks.schemas import TaskCreateSchema
from app.tasks.service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/")
async def get_all_tasks(
    task_service: TaskService = Depends(get_task_service),
):
    return await task_service.get_tasks()


@router.get("/{task_id}")
async def get_task(task_id: int, task_logic: TaskLogic = Depends(get_task_logic)):
    return await task_logic.get_task(task_id)


@router.post("/")
async def create_task(
    body: TaskCreateSchema,
    user_id: int = Depends(get_request_user_id),
    task_logic: TaskLogic = Depends(get_task_logic),
):
    task_id = await task_logic.create_task(body, user_id)
    task = await task_logic.get_task(task_id)
    return {"message": f"Task with id - {task} created successfully"}


@router.put("/{task_id}")
async def update_task(
    task_id: int,
    name: str,
    task_logic: TaskLogic = Depends(get_task_logic),
    user_id: int = Depends(get_request_user_id),
):
    try:
        await task_logic.update_task(task_id, name, user_id)
        return {"message": f"Task with id - {task_id} updated successfully"}
    except TaskNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)


@router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    task_logic: TaskLogic = Depends(get_task_logic),
    user_id: int = Depends(get_request_user_id),
):
    try:
        await task_logic.delete_task(task_id=task_id, user_id=user_id)
    except TaskNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)
    return {"message": "Task deleted successfully"}
