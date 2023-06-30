import torch
from transformers import BertTokenizer, BertForMaskedLM

def reformulate_sentence(sentence):
    # Charger le tokenizer et le modèle BERT pré-entraîné
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForMaskedLM.from_pretrained('bert-base-uncased')

    # Prétraiter la phrase en ajoutant les tokens spéciaux [CLS] et [SEP]
    input_ids = tokenizer.encode("[CLS]" + sentence + "[SEP]", add_special_tokens=True)

      # Convertir les IDs des tokens en tenseurs PyTorch
    input_ids = torch.tensor([input_ids])
    
    # Obtenir les prédictions du modèle BERT
    with torch.no_grad():
        outputs = model(input_ids)
        predictions = outputs[0]
    
    # Trouver l'index du token masqué ([MASK]) dans la phrase
    masked_index = input_ids[0].tolist().index(tokenizer.mask_token_id)
    
    # Obtenir les scores de prédiction pour le token masqué
    masked_token_predictions = predictions[0, masked_index].topk(5)  # Top 5 des prédictions
    
    # Convertir les IDs des tokens prédits en mots
    predicted_tokens = tokenizer.convert_ids_to_tokens(masked_token_predictions.indices.tolist())
    
    return predicted_tokens

