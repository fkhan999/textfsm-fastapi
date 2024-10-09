from io import StringIO
import textfsm
from app.schemas.textfsm_schema import TextFSMRequest

def parse_textfsm(request: TextFSMRequest):
    template_text = request.fsmtxt
    input_text = request.inputtext
    fsmmode = request.fsmmode

    template = textfsm.TextFSM(StringIO(template_text))

    if fsmmode == "true":
        parsed_content = {
            "headers": template.header,
            "values": template.ParseText(input_text),
        }
    else:
        parsed_content = template.ParseTextToDicts(input_text)
    
    return parsed_content
