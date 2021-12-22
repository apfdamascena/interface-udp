# interface-udp

## Interface part

- [x] Deve existir uma rótulo com o nome do programa;
- [x] Deve existir um campo para digitar a mensagem;
- [x] Deve existir um botão de enviar, que pega a mensagem que foi digitada, envia ao destinatário e limpa o campo de digitação, para que o usuário possa digitar outra mensagem em seguida;
- [x] Deve haver a possibilidade de enviar mensagens através da tecla “Enter”, funcionando de modo semelhante ao botão de enviar.
- [x] Deve existir uma área em que as mensagens enviadas sejam visualizadas, e cada mensagem deve ser exibida com sua hora de envio;
Não devem ser enviadas mensagens vazias nem mensagens em branco;
- [x] Deve existir um botão que limpa o chat.
- [x] Deve ser possível o envio de anexo através de um botão, onde será possível escolher um arquivo do computador do usuário e enviá-lo ao destinatário. Esse arquivo poderá ser um vídeo, foto ou música.
- [x] Deve haver no chat a visualização do arquivo enviado. Por exemplo: exibir a miniatura da imagem ou a possibilidade de reproduzir o vídeo, ou música escolhida.  

## Connection part

- [x] Chat será assíncrono, de modo que não haverá necessidade de correspondência entre os usuários
- [x] Ambos deverão estar conectados para que não haja perda de pacotes no processo
- [x] Todas as mensagens enviadas deverão estar presentes no diretório do destinatário ao final da conversação, incluindo as imagens, vídeos e músicas
- [x] Não será obrigatório o uso de um servidor para enviar aos usuários o IP e número de porta, assim, você poderá escolher esses dados conforme sua preferência.
