from pydantic import BaseModel, Field
from typing import Optional, Union, List, Dict, Any, Literal


class Character(BaseModel):
    name: str = Field(description="角色名称", example="Elon musk")
    alias: Optional[List[str]] = Field(default_factory=list, description="角色别称、昵称", example="Elon")
    gender: Optional[str] = Field(default=None, description="Female, Male, or Other. If not mentioned, then None.", example="Male")
    age: Optional[Union[str, int]] = Field(default=None, description="Age number or description. If not mentioned, then None.", examples="Young adult")
    appearance: Optional[str] = Field(default=None, description="The inherent appearance characteristics of the character, such as facial features, face shape, body shape, etc.", example="Orange long hair, deep eyes")
    personality: Optional[str] = Field(default=None, description="Personality traits, interests and hobbies, dislikes, speech patterns and catchphrases, habitual gestures, and body language. If not mentioned, then None.", example=None)
    background: Optional[str] = Field(default=None, description="角色的背景设定，例如职业、教育背景、家庭背景等", example="Single, parents divorced, sophomore in college")
    value_and_beliefs: Optional[str] = Field(default=None, description="Values, beliefs and more principles. If not mentioned, then None.", example="Non-religious, longing for freedom")
    summary: Optional[str] = Field(default=None, description="character introduction less than 3 sentences, concise but distinctive")

class Dialogue(BaseModel):
    '''对话(Dialogue)是帧(Frame)中的一个信息，可以是某些角色之间的"对话"或"内心独白"
    - "对话"指角色与其他角色对话，对应角色有且只有一个
    - "内心独白"指角色内心活动，对应的角色有且只有一个'''
    type: Literal["对话", "内心"]
    character_names: Optional[List[str]] = Field(default_factory=list)
    content: str = Field(description="对话内容、内心独白内容，需与原文保持完全一致。")

class Frame(BaseModel):
    '''帧(Frame)是场景(Scene)中的一个片段，必须包含"视觉背景"，可能包含某些多个"对话"或"内心独白"
    - "视觉背景"是一段视觉场景的描述，对应背景中的角色可以是零个或多个，需要将对应的环境场景使用文字输出,角色对话或独白时的人物描写'''
    type: Literal["视觉背景"]
    character_names: Optional[List[str]] = Field(default_factory=list)
    content: str = Field(description="当前场景下的视觉背景，需与原文保持完全一致。")
    dialogues:List[Dialogue]
      
    
class Scene(BaseModel):
    '''场景(Scene)指故事中发生一段连续剧情，一般场景中的一些要素是连续的，例如地点、时间或人物。场景可能是多个frame组成的，每一帧(frame)是一小段情节的描述，例如一支军队的行军过程，每一帧(frame)是对行军过程中的一个场景剧情的说明'''
    frames:List[Frame]

class KeyObject(BaseModel):
    '''小说中被反复提及的关键对象，可能是物品、环境场景或其他'''
    name: str = Field(description="关键对象的名称")
    alias: Union[List[str]] = Field(default_factory=list, description="关键对象的别称")
    description: str = Field(default=None, description="关键对象的详细描述")


class NovelChunk(BaseModel):
    scenes: List[Scene]
    key_objects: Optional[List[KeyObject]]
    characters: Optional[List[Character]]
