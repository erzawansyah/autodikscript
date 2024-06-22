from modules.ai.image_prompter import create_prompt_from_paragraph


def prompting(paragraph: str, prompt_count: int = 4):
    return create_prompt_from_paragraph(paragraph, prompt_count)
