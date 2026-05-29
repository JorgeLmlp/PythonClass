import math
from flask import render_template, request


def calcular():
    num1_valor = request.form.get("num1", "").strip()
    operacao = request.form.get("operacao")

    if not num1_valor:
        return render_template(
            "index.html",
            etapas="Informe o primeiro número.",
            resultado=""
        )

    num1 = float(num1_valor)

    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro"
            etapas = f"Não existe raiz real de {num1}."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"

    elif operacao == "log":
        if num1 <= 0:
            resultado = "Erro"
            etapas = "O logaritmo só existe para números positivos."
        else:
            resultado = math.log10(num1)
            etapas = f"log({num1}) = {resultado}"

    else:
        num2_valor = request.form.get("num2", "").strip()

        if not num2_valor:
            return render_template(
                "index.html",
                etapas="Informe o segundo número para esta operação.",
                resultado=""
            )
        num2 = float(num2_valor)
    


        num2 = float(num2_valor)

        if operacao == "+":
            resultado = num1 + num2
            etapas = f"{num1} + {num2} = {resultado}"

        elif operacao == "-":
            resultado = num1 - num2
            etapas = f"{num1} - {num2} = {resultado}"

        elif operacao == "*":
            resultado = num1 * num2
            etapas = f"{num1} * {num2} = {resultado}"

        elif operacao == "/":
            if num2 == 0:
                resultado = "Erro"
                etapas = "Divisão por zero não é permitida."
            else:
                resultado = num1 / num2
                etapas = f"{num1} / {num2} = {resultado}"

        elif operacao == "**":
            resultado = num1 ** num2
            etapas = f"{num1}^{num2} = {resultado}"

        elif operacao == "bhaskara":
            num3_valor = request.form.get('num3', '').strip()

            if not num3_valor:
                return render_template(
                "index.html",
                etapas="Informe o terceiro número para esta operação.",
                resultado=""
            )
            num3 = float(num3_valor)
           
           
            a = num1
            b = num2
            c = num3
            
            b = num2 ** 2
            
            delta = b -4 * a * c
            
            if delta < 0:
                resultado = "erro"
                etapas = "impossivel calcular uma equação quando delta é menor que 0"
                
            else:
                resultadoX1 = (-b + math.sqrt(num2)) /2* a
                resultadoX2 = (-b - math.sqrt(num2)) /2 * a
                resultadoX1 = round(resultadoX1, 3)
                resultadoX1 = round(resultadoX2, 3)
                if resultadoX1 == resultadoX2:
                    etapas = f" (-{b} +- √{delta}) /2 * {a}"
                    resultado = resultadoX1
                else:
                    resultado = f"x1 = {resultadoX1} \n x2 = {resultadoX2}"
                    etapas = etapas = f" (-{b} +- √{delta}) /2 * {a}  " 
                
            
            

        else:
            resultado = "Erro"
            etapas = "Operação inválida."

    return render_template(
        "index.html",
        resultado=resultado,
        etapas=etapas
    )