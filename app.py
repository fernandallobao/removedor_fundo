from rembg import remove
from PIL import Image
import flet as ft

def main(page: ft.Page):
    campo_imagem = ft.TextField(label='Informe o nome da imagem com a extensão ou "Enter" para encerrar o programa.')

    def acao(e):
        imagem = campo_imagem.value
        if imagem:
            try:
                nova_img = f'nova_{imagem}'
                original = Image.open(imagem)
                img_sem_fundo = remove(original, bgcolor=(255, 255, 255, 255))
                img_sem_fundo.save(nova_img)
                page.add(ft.Text(f'Imagem salva como: {nova_img}'))
            except Exception as ex:
                page.add(ft.Text(f'Erro: {ex}'))
        else:
            page.add(ft.Text('Por favor, informe um nome de imagem.'))

        page.update()

    botao = ft.ElevatedButton(
        'Retirar fundo',
        bgcolor='green',  # Cor do botão
        color='white',    # Cor do texto
        elevation=10,
        on_click=acao
    )

    page.add(
        ft.Row(
            [ft.Text('Removedor de fundo!', size=40, weight='bold')],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        campo_imagem,
        ft.Row(
            [botao], 
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.update()

ft.app(main)
