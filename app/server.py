from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel
import io
import csv
import uvicorn
from services.helper_functions import list_to_soldier_object, assign_rooms

app = FastAPI()


@app.post("/assignWithCsv")
def upload_soldier_csv(uploaded_file: UploadFile):

    if uploaded_file.content_type != "text/csv":
         return {"error": "File must be a CSV"}

    content = uploaded_file.file.read().decode("utf-8")
    unsorted_list_of_soldiers = []

    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)

    for line in rows:
        soldier = list_to_soldier_object(line)
        if soldier:
            unsorted_list_of_soldiers.append(soldier)

    sorted_list_of_soldiers = sorted(unsorted_list_of_soldiers, key=lambda soldier: soldier.distance_from_base, reverse=True)

    assign_rooms(sorted_list_of_soldiers, army_base)


    return {
        "soldiers_with_rooms": assined_soldiers,
        "waiting_list": waiting_list,
        "total_soldiers": len(sorted_list_of_soldiers),
    }

uvicorn.run(app)

