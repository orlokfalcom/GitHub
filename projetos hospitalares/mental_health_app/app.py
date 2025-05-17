import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from datetime import datetime

class MentalHealthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mental Health App")
        self.root.geometry("600x500")
        self.root.configure(bg="#f1f1f1")
        
        self.user_data = {
            "nome": "", "email": "", "usuario": "", "nascimento": "", 
            "foto": None, "caracteristicas": {}, "diagnostico": "", "exercicios": []  # Adicionando exercícios ao dicionário
        }

        self.create_widgets()

    def create_widgets(self):
        self.clear_screen()
        tk.Label(self.root, text="Bem-vindo ao App de Saúde Mental", font=("Helvetica", 18, "bold"), bg="#f1f1f1").pack(pady=20)
        tk.Button(self.root, text="Iniciar Cadastro", command=self.start_registration, bg="#4CAF50", fg="white").pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def start_registration(self):
        self.clear_screen()
        tk.Label(self.root, text="Cadastro", font=("Helvetica", 18, "bold"), bg="#f1f1f1").pack(pady=10)

        tk.Label(self.root, text="Nome:", bg="#f1f1f1").pack()
        nome_entry = tk.Entry(self.root)
        nome_entry.pack()

        tk.Label(self.root, text="Email:", bg="#f1f1f1").pack()
        email_entry = tk.Entry(self.root)
        email_entry.pack()

        tk.Label(self.root, text="Nome de Usuário:", bg="#f1f1f1").pack()
        usuario_entry = tk.Entry(self.root)
        usuario_entry.pack()

        tk.Label(self.root, text="Data de Nascimento (dd/mm/yyyy):", bg="#f1f1f1").pack()
        nascimento_entry = tk.Entry(self.root)
        nascimento_entry.pack()

        def upload_photo():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
            if file_path:
                self.user_data["foto"] = Image.open(file_path)

        tk.Button(self.root, text="Enviar Foto", command=upload_photo).pack(pady=5)

        def save_registration():
            nome = nome_entry.get()
            email = email_entry.get()
            usuario = usuario_entry.get()
            nascimento = nascimento_entry.get()

            if not nome or not email or not usuario or not nascimento:
                messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
                return  # Não prossegue se algum campo estiver vazio

            self.user_data["nome"] = nome
            self.user_data["email"] = email
            self.user_data["usuario"] = usuario
            self.user_data["nascimento"] = nascimento
            self.ask_questions()

        tk.Button(self.root, text="Salvar e Continuar", command=save_registration, bg="#2196F3", fg="white").pack(pady=20)

    def ask_questions(self):
        self.clear_screen()
        tk.Label(self.root, text="Preencha o Formulário", font=("Helvetica", 18, "bold"), bg="#f1f1f1").pack(pady=10)

        questions = [
            "O que pensa e sente?",
            "O que ouve?",
            "O que vê?",
            "O que fala e faz?",
            "Quais são as dores?",
            "Quais são as necessidades?"
        ]

        answers = {}

        for question in questions:
            tk.Label(self.root, text=question, bg="#f1f1f1").pack()
            answer_entry = tk.Entry(self.root)
            answer_entry.pack(pady=5)
            answers[question] = answer_entry

        def submit_answers():
            # Verificar se todos os campos foram preenchidos
            for question, entry in answers.items():
                if not entry.get():
                    messagebox.showerror("Erro", f"O campo '{question}' é obrigatório.")
                    return  # Não prossegue se algum campo estiver vazio
                self.user_data["caracteristicas"][question] = entry.get()

            # Gerar o diagnóstico automaticamente ao enviar as respostas
            self.generate_diagnosis()
            self.generate_exercises()  # Gerar exercícios com base no diagnóstico
            self.show_profile_screen()  # Mostrar o perfil atualizado com diagnóstico e exercícios

        tk.Button(self.root, text="Enviar", command=submit_answers, bg="#FF9800", fg="white").pack(pady=20)

    def generate_diagnosis(self):
        # Analisar as respostas para gerar o diagnóstico
        caracteristicas = self.user_data["caracteristicas"]
        diagnostico = "Diagnóstico: "

        # Definindo palavras-chave para análise
        keywords = {
            "triste": "Possível depressão.",
            "ansioso": "Possível transtorno de ansiedade.",
            "dor": "Possíveis questões físicas e emocionais.",
            "necessidade": "Necessidade de suporte psicológico."
        }

        found_diagnosis = False  # Flag para verificar se encontramos algo relacionado

        # Percorre as respostas e verifica as palavras-chave
        for question, answer in caracteristicas.items():
            for word, possible_diagnosis in keywords.items():
                if word in answer.lower():  # Verifica se a palavra-chave está na resposta
                    diagnostico += possible_diagnosis + " "
                    found_diagnosis = True

        # Se não encontrar palavras-chave, coloca um diagnóstico padrão
        if not found_diagnosis:
            diagnostico = "Sem diagnóstico no momento."

        self.user_data["diagnostico"] = diagnostico  # Armazenar o diagnóstico no perfil do usuário

    def generate_exercises(self):
        # Exercícios baseados no diagnóstico
        diagnostico = self.user_data["diagnostico"]
        exercises = []

        if "depressão" in diagnostico.lower():
            exercises = [
                "Exercício 1: Caminhada de 20 minutos ao ar livre.",
                "Exercício 2: Escrever sobre seus sentimentos por 10 minutos.",
                "Exercício 3: Praticar técnicas de respiração profunda."
            ]
        elif "ansiedade" in diagnostico.lower():
            exercises = [
                "Exercício 1: Prática de meditação de 10 minutos.",
                "Exercício 2: Técnica de respiração 4-7-8.",
                "Exercício 3: Alongamento simples por 15 minutos."
            ]
        elif "dor" in diagnostico.lower():
            exercises = [
                "Exercício 1: Fazer uma massagem relaxante nas mãos e pés.",
                "Exercício 2: Praticar yoga suave.",
                "Exercício 3: Respirar profundamente por 5 minutos."
            ]
        elif "necessidade de suporte psicológico" in diagnostico.lower():
            exercises = [
                "Exercício 1: Conversar com um amigo ou terapeuta sobre suas emoções.",
                "Exercício 2: Praticar afirmações positivas diariamente.",
                "Exercício 3: Participar de grupos de apoio online."
            ]
        else:
            exercises = [
                "Exercício 1: Aumentar a atividade física diária.",
                "Exercício 2: Praticar hobbies criativos como desenho ou escrita.",
                "Exercício 3: Tentar novos hábitos de relaxamento."
            ]

        self.user_data["exercicios"] = exercises  # Armazenar os exercícios no perfil do usuário

    def calculate_age(self, nascimento):
        try:
            birth_date = datetime.strptime(nascimento, "%d/%m/%Y")
            today = datetime.today()
            age = today.year - birth_date.year
            if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
                age -= 1
            return age
        except ValueError:
            return "Data inválida"

    def show_profile_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Perfil do Usuário", font=("Helvetica", 18, "bold"), bg="#f1f1f1").pack(pady=10)

        if isinstance(self.user_data["foto"], Image.Image):
            try:
                img = ImageTk.PhotoImage(self.user_data["foto"].resize((100, 100)))
                img_label = tk.Label(self.root, image=img, bg="#f1f1f1")
                img_label.image = img
                img_label.pack(pady=10)
            except Exception as e:
                print(f"Erro ao exibir imagem do perfil: {e}")

        for key in ["nome", "email", "usuario", "nascimento"]:  # Exibe a data de nascimento
            tk.Label(self.root, text=f"{key.capitalize()}: {self.user_data[key]}", bg="#f1f1f1", font=("Helvetica", 12)).pack()

        # Exibe a idade calculada a partir da data de nascimento
        age = self.calculate_age(self.user_data["nascimento"])
        tk.Label(self.root, text=f"Idade: {age}", bg="#f1f1f1", font=("Helvetica", 12)).pack(pady=10)
        
        tk.Label(self.root, text=f"Diagnóstico: {self.user_data['diagnostico']}", bg="#f1f1f1", font=("Helvetica", 12)).pack(pady=10)

        tk.Label(self.root, text="Exercícios recomendados:", bg="#f1f1f1", font=("Helvetica", 12, "bold")).pack(pady=10)

        for exercise in self.user_data["exercicios"]:
            tk.Label(self.root, text=exercise, bg="#f1f1f1", font=("Helvetica", 12)).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MentalHealthApp(root)
    root.mainloop()
