import customtkinter as ctk
import tkinter.messagebox as messagebox
from db import conectar

class CadastroPaciente(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Paciente")
        self.geometry("400x400")

        self.label_nome = ctk.CTkLabel(self, text="Nome")
        self.label_nome.pack()
        self.entry_nome = ctk.CTkEntry(self)
        self.entry_nome.pack()

        self.label_cpf = ctk.CTkLabel(self, text="CPF")
        self.label_cpf.pack()
        self.entry_cpf = ctk.CTkEntry(self)
        self.entry_cpf.pack()

        self.label_nasc = ctk.CTkLabel(self, text="Data de Nascimento (AAAA-MM-DD)")
        self.label_nasc.pack()
        self.entry_nasc = ctk.CTkEntry(self)
        self.entry_nasc.pack()

        self.label_sintomas = ctk.CTkLabel(self, text="Sintomas")
        self.label_sintomas.pack()
        self.entry_sintomas = ctk.CTkEntry(self)
        self.entry_sintomas.pack()

        self.btn_salvar = ctk.CTkButton(self, text="Salvar", command=self.salvar_paciente)
        self.btn_salvar.pack(pady=10)

    def salvar_paciente(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO pacientes (nome, cpf, nascimento, sintomas)
                VALUES (%s, %s, %s, %s)
            """, (
                self.entry_nome.get(),
                self.entry_cpf.get(),
                self.entry_nasc.get(),
                self.entry_sintomas.get()
            ))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sucesso", "Paciente cadastrado com sucesso.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", str(e))