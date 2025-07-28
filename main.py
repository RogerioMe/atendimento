import customtkinter as ctk
from cadastro import CadastroPaciente
from triagem import TriagemPaciente
from atendimento import AtendimentoPaciente
from relatorio import RelatorioPaciente

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Atendimento UPA")
        self.geometry("500x400")
        ctk.set_appearance_mode("light")

        self.label = ctk.CTkLabel(self, text="Menu Principal", font=("Arial", 20))
        self.label.pack(pady=20)

        self.btn_cadastrar = ctk.CTkButton(self, text="Cadastrar Paciente", command=self.abrir_cadastro)
        self.btn_cadastrar.pack(pady=10)

        self.btn_triagem = ctk.CTkButton(self, text="Triagem", command=self.abrir_triagem)
        self.btn_triagem.pack(pady=10)

        self.btn_atendimento = ctk.CTkButton(self, text="Atendimento", command=self.abrir_atendimento)
        self.btn_atendimento.pack(pady=10)

        self.btn_relatorio = ctk.CTkButton(self, text="Relatório", command=self.abrir_relatorio)
        self.btn_relatorio.pack(pady=10)

    def abrir_cadastro(self):
        CadastroPaciente()

    def abrir_triagem(self):
        TriagemPaciente()

    def abrir_atendimento(self):
        AtendimentoPaciente()

    def abrir_relatorio(self):
        RelatorioPaciente()

if __name__ == "__main__":
    app = App()
    app.mainloop()
