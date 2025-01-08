listagem_de_tarefas=[] #aqui ficarão armazenadas todas as tarefas em formato de dicionário, fazendo assim um dicionério de listas

print('     Bem-Vindo ao Gerenciador de Tarefas     ') #estética

print('O que você deseja fazer hoje?') #introduzir os comandos ao usuário

print('Editar(edit)')#check
print('Visualisar(view)')#check
print('Adicionar(add)')#check
print('Remover(remove)')#check
print('Marcar como concluída(check)')#check
print('Visualisar tudo (visar tudo)')#check
#comandos para o usuário

entrar=input('você quer entrar?') #aqui eu ainda tenho que concertar, pois qualquer coisa != de não entra no programa

while entrar !='não': #inicia um laço infinito q só quebra com uma condição
    print('Digite o comando + nome da tarefa(para sair digite (sair app):')#mais comandos
    comando, nome_tarefa=input().split('--') #a resposta do usuário é dividida em duas variáveis: a primeira é o comando e a segunda o nome da tarefa
    if comando=='sair' and nome_tarefa=='app': #essa condicional existe justamente pq o laço é infinito. quando o usuário já não tiver mais tarefas para adicionar, irá mandar um 'sair app' e o programa se incerrará
        print('tchau')#mensagem pra indicar o fim do programa
        break

    else: #caso contrário, o laço se repete

        if comando=='add':
            nova_tarefa={} #criasse um dicionário vazio 
            nova_tarefa['Título']= nome_tarefa #como a resposta do usuário foi dividida em duas variáveis, uma delas foi o nome da tarefa
            descrição_tarefa=input('adicone uma breve descrição:') #descreve o objetivo da tarefa
            nova_tarefa['Descrição']= descrição_tarefa #adiciona ao dicionário
            prioridade=input('proridade alta, media ou baixa?') #armazena a prioridade
            nova_tarefa['Prioridade']= prioridade #adiciona a prioridade
            situação=input('Essa tarefa está pendente ou concluída?')
            nova_tarefa['Situação']=situação
            copia= nova_tarefa.copy() #faz uma cópia dessa resposta para armazenar na lista, assim evita de sobreescrever os dados anteriores
            listagem_de_tarefas.append(copia) #adiciona a copia à lista
            print(nova_tarefa) #mostra a nova tarefa
            
        elif comando =='remove':
            for item in list(listagem_de_tarefas):
                if item['Título']==nome_tarefa:
                    listagem_de_tarefas.remove(item)
                    print('Tarefa removida com sucesso')
                else:
                     print('Tarefa não removida ou não existe')
                
                
        elif comando =='visar' and nome_tarefa=='tudo': #aqui é só para mostrar todas as tarefas existentes
            for i in listagem_de_tarefas:
                if i['Situação']=='concluida':
                    print('CONCLUÍDA')
                    print(i)
                elif i['Situação']=='pendente':
                    print('PENDENTE')
                    print(i)

#Dia 2 (08/01/2025)- fazer pelo menos o comando Editar

        elif comando=='edit':
            for i in listagem_de_tarefas:
                if i.get('Título')== nome_tarefa:
                    nova_desc=input('Insira a nova descrição')
                    i['Descrição']=nova_desc
                    print(i)

        elif comando=='check':
            for i in listagem_de_tarefas:
                if i.get('Título')==nome_tarefa and i.get('Situação')=='pendente': 
                        i['Situação']='concluída'
                        print(i)

        elif comando=='view':
             for i in listagem_de_tarefas:
                if i['Título']==nome_tarefa:
                    print(i)


#DIA 3(09/01/2025)- parte INSUPORTÁVEL do código: condicionais de erro

        
                    

                            
                       
                    

        
       
                
                
