from fastapi import APIRouter


router_model_analysis = APIRouter(
    tags=["Analysis"],
    prefix="/model_analysis"
)

router_model_classification = APIRouter(
    tags=["Classification"],
    prefix="/model_classification"
)

router_model_generation = APIRouter(
    tags=["Generation"],
    prefix="/model_generation"
)


router_preprocess_image = APIRouter(
    tags=["ImagePreprocess"],
    prefix="/preprocess_image"
)

router_preprocess_text = APIRouter(
    tags=["TextPreprocess"],
    prefix="/preprocess_text"
)