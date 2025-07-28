import customtkinter as ctk
import tkinter.messagebox as messagebox
from db import conectar

class AtendimentoPaciente(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Atendimento")
        self.geometry("400x500")

        self.label_id = ctk.CTkLabel(self, text="ID do Paciente")
        self.label_id.pack()
        self.entry_id = ctk.CTkEntry(self)
        self.entry_id.pack()

        self.label_medico = ctk.CTkLabel(self, text="Nome do Médico")
        self.label_medico.pack()
        self.entry_medico = ctk.CTkEntry(self)
        self.entry_medico.pack()

        self.label_diag = ctk.CTkLabel(self, text="Diagnóstico")
        self.label_diag.pack()
        self.entry_diag = ctk.CTkEntry(self)
        self.entry_diag.pack()

        self.label_presc = ctk.CTkLabel(self, text="Prescrição")
        self.label_presc.pack()
        self.entry_presc = ctk.CTkEntry(self)
        self.entry_presc.pack()

        self.label_status = ctk.CTkLabel(self, text="Status")
        self.label_status.pack()
        self.combo_status = ctk.CTkComboBox(self, values=["Alta", "Internação", "Retorno", "Encaminhado"])
        self.combo_status.pack()

        self.btn_salvar = ctk.CTkButton(self, text="Registrar Atendimento", command=self.salvar_atendimento)
        self.btn_salvar.pack(pady=10)

    def salvar_atendimento(self):
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO atendimentos (paciente_id, medico_nome, diagnostico, prescricao, status)
                VALUES (%s, %s, %s, %s, %s)
            """, (
                self.entry_id.get(),
                self.entry_medico.get(),
                self.entry_diag.get(),
                self.entry_presc.get(),
                self.combo_status.get()
            ))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Sucesso", "Atendimento registrado.")
            self.destroy()
        except Exception as e:
            messagebox.showerror("Erro", str(e))