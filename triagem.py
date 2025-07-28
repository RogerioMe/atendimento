import customtkinter as ctk
import tkinter.messagebox as messagebox
from db import conectar

class TriagemPaciente(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Triagem")
        self.geometry("400x400")

        self.label_id = ctk.CTkLabel(self, text="ID do Paciente")
        self.label_id.pack()
        self.entry_id = ctk.CTkEntry(self)
        self.entry_id.pack()

        self.label_risco = ctk.CTkLabel(self, text="Nível de Risco")
        self.label_risco.pack()
        self.combo_risco = ctk.CTkComboBox(self, values=["Vermelho", "Laranja", "Amarelo", "Verde", "Azul"])
        self.combo_risco.pack()

        self.label_setor = ctk.CTkLabel(self, text="Setor")
        self.label_setor.pack()
        self.entry_setor = ctk.CTkEntry(self)
        self.entry_setor.pack()

        self.btn_salvar = ctk.CTkButton(self, text="Registrar Triagem", command=self.registrar_triagem)
        self.btn_salvar.pack(pady=10)

    def registrar_triagem(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO triagens (paciente_id, nivel_risco, setor)
                VALUES (%s, %s, %s)
            """, (
                self.entry_id.get(),
                self.combo_risco.get(),
                self.entry_setor.get()
            ))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sucesso", "Triagem registrada.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", str(e))
''