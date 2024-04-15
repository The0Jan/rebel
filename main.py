from transformers import pipeline

triplet_extractor = pipeline('text2text-generation', model='E:/CodesRepos/MGR_Gaming/Model/rebel/model/Rebel-self_personal', tokenizer='E:/CodesRepos/MGR_Gaming/Model/rebel/model/Rebel-self_personal')

# We need to use the tokenizer manually since we need special tokens.
triplets = triplet_extractor("Marie has a sister, whose name is Claire.", return_tensors=True, return_text=False)[0]["generated_token_ids"]["output_ids"][0]
extracted_text = triplet_extractor.tokenizer.batch_decode(triplets)

print(extracted_text)

# Function to parse the generated text and extract the triplets
def extract_triplets(text):
    triplets = []
    relation, subject, relation, object_ = '', '', '', ''
    text = text.strip('')
    current = 'x'
    for token in text.replace("<s>", "").replace("<pad>", "").replace("</s>", "").replace("<", " ").replace(">", " ").split():
        if token == "triplet":
            current = 't'
            if relation != '':
                triplets.append({'head': subject.strip(), 'type': relation.strip(),'tail': object_.strip()})
                relation = ''
            subject = ''
        elif token == "subj":
            current = 's'
            if relation != '':
                triplets.append({'head': subject.strip(), 'type': relation.strip(),'tail': object_.strip()})
            object_ = ''
        elif token == "obj":
            current = 'o'
            relation = ''
        else:
            if current == 't':
                subject += ' ' + token
            elif current == 's':
                object_ += ' ' + token
            elif current == 'o':
                relation += ' ' + token
    if subject != '' and relation != '' and object_ != '':
        triplets.append({'head': subject.strip(), 'type': relation.strip(),'tail': object_.strip()})
    return triplets

extracted_triplets = extract_triplets(extracted_text[0])
print(extracted_triplets)