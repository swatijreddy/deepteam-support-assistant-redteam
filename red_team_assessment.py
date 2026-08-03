

from deepteam import red_team
from deepteam.vulnerabilities import Toxicity, Bias, PIILeakage, PromptLeakage
from deepteam.attacks.single_turn import PromptInjection, Roleplay

from callback_wrapper import my_target_wrapper




bias = Bias(types=["race"])
pii_leakage = PIILeakage(types=["api_and_database_access"])
toxicity = Toxicity(types=["insults"])
prompt_leakage = PromptLeakage(types=["secrets_and_credentials", "guard_exposure"])

prompt_injection = PromptInjection(weight=2)
role_play = Roleplay(weight=1)


risk_assessment = red_team(
    model_callback = my_target_wrapper,
    vulnerabilities=[bias,pii_leakage,toxicity,prompt_leakage],
    attacks=[prompt_injection,role_play],
    attacks_per_vulnerability_type=3
)

