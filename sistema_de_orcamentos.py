import locale
from fpdf import FPDF

# Defina a localização para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

project = input("Digite a Descrição do projeto:  ");
predicted_hours = input("Digite a quantidade de horas previstas: ");
hours_Value = input("Digite o valor da hora trabalhada: ");
worked_hours = int(hours_Value)
term = input("Digite o prazo: ");
total_value = int(predicted_hours) * int(worked_hours)

print(project);
print(predicted_hours);
print(worked_hours)
print(term)
print(total_value)


""" Gerando o PDFs do Projetos """

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.image("template.png", x=0, y=0, w=pdf.w, h=pdf.h)

pdf.text(115, 145, project)
pdf.text(115, 160, f"{predicted_hours} horas")

# Formatação das horas trabalhadas como reais (R$)
formatted_worked_hours = locale.currency(worked_hours, grouping=True, symbol=True)
pdf.text(115, 175, formatted_worked_hours)

pdf.text(115, 190, term)

# Formatação do valor em reais (R$)
formatted_total = locale.currency(total_value, grouping=True, symbol=True)
pdf.text(115, 205, formatted_total)

pdf.output("Orçamento.pdf")
print("Orçamento gerado com Sucesso")