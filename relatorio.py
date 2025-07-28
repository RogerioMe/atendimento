import customtkinter as ctk
from tkinter import messagebox
from db import conectar

class RelatorioPaciente(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Relatório de Pacientes")
        self.geometry("600x400")

        self.textbox = ctk.CTkTextbox(self, width=580, height=350)
        self.textbox.pack(pady=10)

        self.btn_gerar = ctk.CTkButton(self, text="Gerar Relatório", command=self.gerar_relatorio)
        self.btn_gerar.pack(pady=10)

    def gerar_relatorio(self):
        try:
            conn = conectar()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT p.id, p.nome, p.cpf, p.nascimento, p.sintomas,
                       t.nivel_risco, t.setor,
                       a.medico_nome, a.diagnostico, a.prescricao, a.status
                FROM pacientes p
                LEFT JOIN triagens t ON p.id = t.paciente_id
                LEFT JOIN atendimentos a ON p.id = a.paciente_id
                ORDER BY p.id
            """)
            dados = cursor.fetchall()
            self.textbox.delete("1.0", "end")
            for d in dados:
                self.textbox.insert("end", f"ID: {d['id']}, Nome: {d['nome']}, CPF: {d['cpf']}\n")
                self.textbox.insert("end", f"Nascimento: {d['nascimento']}, Sintomas: {d['sintomas']}\n")
                self.textbox.insert("end", f"Risco: {d['nivel_risco']}, Setor: {d['setor']}\n")
                self.textbox.insert("end", f"Médico: {d['medico_nome']}, Diagnóstico: {d['diagnostico']}\n")
                self.textbox.insert("end", f"Prescrição: {d['prescricao']}, Status: {d['status']}\n")
                self.textbox.insert("end", "="*60 + "\n")
            cursor.close()
            conn.close()
        except Exception as e:
            messagebox.showerror("Erro", str(e))
