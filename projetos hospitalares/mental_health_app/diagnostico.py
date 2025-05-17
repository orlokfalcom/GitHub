import tkinter as tk
from tkinter import messagebox

# Funções de diagnóstico
def diagnostico(respostas):
    # Análise de sentimentos e palavras-chave (simplificado)
    sentimentos = analisar_sentimentos(respostas['o_que_pensa_e_sente'])
    dores = analisar_dores(respostas['quais_sao_as_dores'])
    necessidades = analisar_necessidades(respostas['quais_sao_as_necessidades'])
    transtornos = diagnosticar_transtornos(respostas)

    # Diagnóstico emocional
    if 'triste' in sentimentos or 'desesperado' in sentimentos:
        estado_emocional = "Tristeza detectada"
    elif 'ansioso' in sentimentos or 'nervoso' in sentimentos:
        estado_emocional = "Ansiedade detectada"
    elif 'deprimido' in sentimentos or 'sem energia' in sentimentos:
        estado_emocional = "Depressão possível"
    else:
        estado_emocional = "Estado emocional estável"

    if dores:
        tipo_dor = "Dores físicas ou emocionais detectadas"
    else:
        tipo_dor = "Sem dores detectadas"

    if necessidades:
        tipo_necessidade = "Necessidades emocionais ou de suporte identificadas"
    else:
        tipo_necessidade = "Sem necessidades identificadas"

    # Concatenando diagnóstico
    diagnostico_completo = f"Diagnóstico: {estado_emocional}, {tipo_dor}, {tipo_necessidade}. Possíveis transtornos: {', '.join(transtornos)}"
    
    return diagnostico_completo

def analisar_sentimentos(texto):
    # Análise de sentimentos detalhada
    sentimentos_possiveis = ['triste', 'desesperado', 'ansioso', 'nervoso', 'deprimido', 'sem energia', 'feliz', 'grato']
    sentimentos_detectados = [sentimento for sentimento in sentimentos_possiveis if sentimento in texto.lower()]
    return sentimentos_detectados if sentimentos_detectados else ['normal']

def analisar_dores(texto):
    # Identificação de dores físicas e emocionais
    dores_fisicas = ['dor de cabeça', 'dores no corpo', 'cansaço', 'dormência']
    dores_emocionais = ['tristeza profunda', 'sofrendo emocionalmente', 'angústia']
    
    dores_detectadas = [dor for dor in dores_fisicas + dores_emocionais if dor in texto.lower()]
    return dores_detectadas

def analisar_necessidades(texto):
    # Identificação de necessidades emocionais e físicas
    necessidades_emocionais = ['ajuda', 'suporte', 'acolhimento', 'compreensão']
    necessidades_fisicas = ['alimento', 'descanso', 'atendimento médico']
    
    necessidades_detectadas = [necessidade for necessidade in necessidades_emocionais + necessidades_fisicas if necessidade in texto.lower()]
    return necessidades_detectadas

def diagnosticar_transtornos(respostas):
    transtornos_detectados = []

    # Transtornos de Ansiedade
    ansiedade_keywords = [
        "fobia", "síndrome do pânico", "ansiedade generalizada", "ansiedade social", "ansiedade por separação", "medo constante"
    ]
    if any(keyword in respostas['o_que_pensa_e_sente'].lower() for keyword in ansiedade_keywords):
        transtornos_detectados.append("Transtornos de Ansiedade")

    # Transtornos de Humor
    humor_keywords = [
        "depressão", "transtorno bipolar", "distimia", "transtorno afetivo bipolar", "transtorno de humor disfórico", "sentimentos intensos"
    ]
    if any(keyword in respostas['o_que_pensa_e_sente'].lower() for keyword in humor_keywords):
        transtornos_detectados.append("Transtornos de Humor")

    # Transtornos Psicóticos
    psicotico_keywords = ["esquizofrenia", "transtorno delirante", "transtorno psicótico breve"]
    if any(keyword in respostas['o_que_pensa_e_sente'].lower() for keyword in psicotico_keywords):
        transtornos_detectados.append("Transtornos Psicóticos")

    # Transtornos de Personalidade
    personalidade_keywords = [
        "borderline", "antisocial", "narcisista", "evitativa", "dependente", "paranoide", "esquizoide", "histriônica", "autossuficiente"
    ]
    if any(keyword in respostas['o_que_pensa_e_sente'].lower() for keyword in personalidade_keywords):
        transtornos_detectados.append("Transtornos de Personalidade")

    # Transtornos de Desenvolvimento
    desenvolvimento_keywords = ["autista", "tdah", "déficit de atenção", "deficiência intelectual"]
    if any(keyword in respostas['o_que_pensa_e_sente'].lower() for keyword in desenvolvimento_keywords):
        transtornos_detectados.append("Transtornos de Desenvolvimento")

    # Transtornos Alimentares
    alimentar_keywords = ["anorexia", "bulimia", "compulsão alimentar"]
    if any(keyword in respostas['o_que_pensa_e_sente'].lower() for keyword in alimentar_keywords):
        transtornos_detectados.append("Transtornos Alimentares")

    # Transtornos Neurocognitivos
    neurocognitivo_keywords = ["alzheimer", "parkinson", "demência"]
    if any(keyword in respostas['o_que_pensa_e_sente'].lower() for keyword in neurocognitivo_keywords):
        transtornos_detectados.append("Transtornos Neurocognitivos")

    # Outros Transtornos
    outros_keywords = [
        "toque", "estresse pós-traumático", "insônia", "apneia do sono", "dependência de álcool", "drogas"
    ]
    if any(keyword in respostas['o_que_pensa_e_sente'].lower() for keyword in outros_keywords):
        transtornos_detectados.append("Outros Transtornos")

    return transtornos_detectados

class DiagnosticoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Autoavaliação de Saúde Mental")
        self.user_data = {
            "respostas": {},
            "reflexao": {},
            "diagnostico": ""
        }
        self.create_interface()

    def create_interface(self):
        # Perguntas
        self.pergunta_label = tk.Label(self.master, text="Como você tem se sentido ultimamente?")
        self.pergunta_label.pack()

        self.resposta_entry = tk.Entry(self.master, width=50)
        self.resposta_entry.pack()

        self.pergunta_dores_label = tk.Label(self.master, text="Você tem sentido alguma dor física ou emocional?")
        self.pergunta_dores_label.pack()

        self.dores_entry = tk.Entry(self.master, width=50)
        self.dores_entry.pack()

        self.pergunta_necessidades_label = tk.Label(self.master, text="Você sente que tem alguma necessidade emocional ou de suporte?")
        self.pergunta_necessidades_label.pack()

        self.necessidades_entry = tk.Entry(self.master, width=50)
        self.necessidades_entry.pack()

        self.enviar_button = tk.Button(self.master, text="Enviar", command=self.coletar_resposta)
        self.enviar_button.pack()

        self.resultado_button = tk.Button(self.master, text="Gerar Diagnóstico", command=self.generate_diagnosis)
        self.resultado_button.pack()

        self.diagnostico_label = tk.Label(self.master, text="", wraplength=400)
        self.diagnostico_label.pack()

    def coletar_resposta(self):
        resposta = self.resposta_entry.get()
        dores = self.dores_entry.get()
        necessidades = self.necessidades_entry.get()
        
        if resposta.strip() and dores.strip() and necessidades.strip():
            # Armazenar as respostas no dicionário de reflexões
            self.user_data["reflexao"]["o_que_pensa_e_sente"] = resposta
            self.user_data["reflexao"]["quais_sao_as_dores"] = dores
            self.user_data["reflexao"]["quais_sao_as_necessidades"] = necessidades

            messagebox.showinfo("Resposta recebida", "Suas respostas foram registradas.")
            self.resposta_entry.delete(0, tk.END)  # Limpar campo de "o que pensa e sente"
            self.dores_entry.delete(0, tk.END)  # Limpar campo de "dores"
            self.necessidades_entry.delete(0, tk.END)  # Limpar campo de "necessidades"
        else:
            messagebox.showerror("Erro", "Todos os campos de resposta devem ser preenchidos.")  # Validação de campos obrigatórios

    def generate_diagnosis(self):
        # Coletar respostas do usuário
        respostas = {
            'o_que_pensa_e_sente': self.user_data["reflexao"].get("o_que_pensa_e_sente", ""),
            'quais_sao_as_dores': self.user_data["reflexao"].get("quais_sao_as_dores", ""),
            'quais_sao_as_necessidades': self.user_data["reflexao"].get("quais_sao_as_necessidades", "")
        }

        diagnostico_resultado = diagnostico(respostas)
        self.user_data["diagnostico"] = diagnostico_resultado
        self.diagnostico_label.config(text="Diagnóstico: " + self.user_data["diagnostico"])

# Criação da janela do tkinter
root = tk.Tk()
app = DiagnosticoApp(root)
root.mainloop()
