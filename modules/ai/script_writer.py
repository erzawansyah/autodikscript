import streamlit as st
from typing import List
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI


class SceneModel(BaseModel):
    subtitle: str = Field(..., description="Subtitle for the scene")
    image: str = Field(..., description="Visual brief for the scene")
    voiceover: str = Field(
        ...,
        description="Voiceover narrative describing the scene. This should be a few sentences long. At least 5 sentences are required.",
    )


class ClosingShotModel(BaseModel):
    closing_shot: str = Field(
        ..., description="Description of the visual setting for the closing shot."
    )
    voiceover: str = Field(..., description="Voiceover narrative for the closing shot.")


class EndScreenModel(BaseModel):
    call_to_action: str = Field(
        ..., description="Call to action encouraging viewer engagement."
    )
    closing_voiceover: str = Field(
        ..., description="Final voiceover message concluding the script."
    )


class ScriptModel(BaseModel):
    hook: str = Field(
        ...,
        description="Intriguing hook to capture viewer attention at the start of the video.",
    )
    body: List[SceneModel] = Field(
        ..., description="List of scenes describing the main content of the video."
    )
    closing: ClosingShotModel = Field(
        ..., description="Closing shot and voiceover for the end of the video."
    )
    cta: EndScreenModel = Field(
        ..., description="End screen with call to action and closing message."
    )


@st.cache_data
def write_script(
    keywords: str,
    title: str,
    notes: str,
    model: str = "gpt-3.5-turbo",
    total_sections: int = 5,
):
    try:
        llm = ChatOpenAI(
            api_key=st.secrets["openai_api_key"],
            model=model,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
        )

        messages = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a youtube script writer. Always return the script in JSON format that includes a hook, body, closing, and cta.",
                ),
                (
                    "human",
                    "Create a 5-minute YouTube video script based on keywords and article titles provided by your content manager. Your script should include a hook that intrigues the audience, a body with at least {total_sections} sections, and a compelling call-to-action (CTA) to make the video go viral."
                    "Here are the details for the script:"
                    "Keywords: {keywords}, Title: {title}, Notes: {notes}",
                ),
            ]
        )

        runnable = messages | llm.with_structured_output(schema=ScriptModel)

        ai_msg = runnable.invoke(
            {
                "keywords": keywords,
                "title": title,
                "notes": notes,
                "total_sections": total_sections,
            }
        )

        return ai_msg
    except Exception as e:
        st.error(f"An error occurred while generating the script: {e}")
        return None
