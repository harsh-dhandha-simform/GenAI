from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
load_dotenv()

class Extract(BaseModel):
    name: str =  Field(description="Person's name")
    location: str = Field(description="Person's city")
    philosophy: str = Field(description="Person's Philosophy")
    year: str = Field(description="Person's Birth Year")
    occupation: str = Field(description="Person's occupation or profession")
    nationality: str = Field(description="Person's nationality")
    notable_works: str = Field(description="Person's notable works or achievements")
    education: str = Field(description="Person's education or academic background")
    parents: str = Field(description="Person's parents")
    spouse: str = Field(description="Person's spouse")
    children: str = Field(description="Person's children")
    awards: str = Field(description="Awards or honors received by the person")
    
model = ChatOpenAI( model = "gpt-4o-2024-08-06", api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))

structured_model=model.with_structured_output(Extract)
    
result = structured_model.invoke(""" 
                                 Aristotle[A] (Ancient Greek: Ἀριστοτέλης, romanized: Aristotélēs;[B] 384–322 BC) was an ancient Greek philosopher and polymath. 
                                 His writings span the natural sciences, philosophy, linguistics, economics, politics, psychology, and the arts.
                                 As the founder of the Peripatetic school of philosophy in the Lyceum in Athens, he began the wider Aristotelian tradition that followed,
                                 which set the groundwork for the development of modern science. Little is known about Aristotle's life.
                                 He was born in the city of Stagira in northern Greece during the Classical period. His father, Nicomachus, died when Aristotle 
                                 was a child, and he was brought up by a guardian. At around eighteen years old, he joined Plato's Academy in Athens and remained 
                                 there until the age of thirty seven (c. 347 BC). Shortly after Plato died, Aristotle left Athens and, at the request of Philip II of Macedon, 
                                 tutored his son Alexander the Great beginning in 343 BC. He established a library in the Lyceum, which helped him to produce 
                                 many of his hundreds of books on papyrus scrolls. """)
print(result)