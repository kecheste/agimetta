from hyperon import *
from hyperon.ext import register_atoms
from .agents import news_agent, sentiment_analysis_agent

@register_atoms(pass_metta=True)
def agimetta_atoms(metta):
    newsAtom = OperationAtom('news', lambda *args: news_agent(metta, *args), [AtomType.ATOM, "Expression"], unwrap=False)
    sentimentAtom = OperationAtom('sentiment', lambda *args: sentiment_analysis_agent(metta, *args), [AtomType.ATOM, "Expression"], unwrap=False)
    
    return {
        "news": newsAtom,
        "sentiment": sentimentAtom
    }