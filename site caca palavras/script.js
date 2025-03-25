document.addEventListener('DOMContentLoaded', () => {
    // Lista de 200 palavras (substitua com suas palavras)
    const allWords = [
    'HTML', 'JAVASCRIPT', 'CSS', 'CODIGO', 'WEBSITE', 'PROGRAMACAO', 'DESENVOLVIMENTO',
    'ALGORITMO', 'FUNCAO', 'VARIAVEL',
    'SERVIDOR', 'BANCODEDADOS', 'REDE', 'INTERNET', 'APLICATIVO', 'SISTEMA',
    'SEGURANCA', 'USUARIO', 'INTERFACE', 'DESIGN',
    'PROJETO', 'EQUIPE', 'GERENCIAMENTO', 'COMUNICACAO', 'CLIENTE', 'REQUISITO', 'TESTE',
    'QUALIDADE', 'IMPLANTACAO', 'MANUTENCAO',
    'ARQUITETURA', 'PADRAO', 'DOCUMENTACAO', 'VERSAO', 'ATUALIZACAO', 'OTIMIZACAO',
    'PERFORMANCE', 'ESCALABILIDADE', 'INOVACAO', 'TECNOLOGIA',
    'COMPUTADOR', 'DISPOSITIVO', 'SOFTWARE', 'HARDWARE', 'CELULAR', 'TABLET', 'LAPTOP',
    'DESKTOP', 'IMPRESSORA', 'MONITOR',
    'TECLADO', 'MOUSE', 'CAIXDESOM', 'MICROFONE', 'WEBCAM', 'PENDRIVE', 'HDEXTERNO',
    'SSD', 'MEMORIA', 'PROCESSADOR',
    'PLACAVIDEO', 'PLACAMAE', 'FONTE', 'GABINETE', 'REFRIGERACAO', 'VENTILADOR',
    'PASTATERMICA', 'DRIVER', 'BIOS', 'FIRMWARE',
    'ANTIVIRUS', 'FIREWALL', 'BACKUP', 'RESTAURACAO', 'FORMATACAO', 'PARTICAO',
    'SISTEMAOPERACIONAL', 'WINDOWS', 'LINUX', 'MACOS',
    'ANDROID', 'IOS', 'NAVEGADOR', 'CHROME', 'FIREFOX', 'SAFARI', 'EDGE', 'PESQUISA',
    'GOOGLE', 'BING',
    'EMAIL', 'REDE SOCIAL', 'FACEBOOK', 'INSTAGRAM', 'TWITTER', 'LINKEDIN', 'YOUTUBE',
    'WHATSAPP', 'TELEGRAM', 'VIDEO',
    'IMAGEM', 'AUDIO', 'TEXTO', 'DOCUMENTO', 'PLANILHA', 'APRESENTACAO', 'PDF', 'ZIP',
    'RAR', 'EXECUTAVEL',
    'VIRTUALIZACAO', 'NUVEM', 'ARMAZENAMENTO', 'SINCRONIZACAO',
    'COMPARTILHAMENTO', 'STREAMING', 'PODCAST', 'WEBCONFERENCIA', 'SEMINARIO', 'CURSO',
    'EDUCACAO', 'APRENDIZADO', 'CONHECIMENTO', 'HABILIDADE', 'COMPETENCIA',
    'CERTIFICACAO', 'DIPLOMA', 'GRADUACAO', 'POSGRADUACAO', 'MESTRADO',
    'DOUTORADO', 'PESQUISA', 'CIENCIA', 'ENGENHARIA', 'MATEMATICA', 'FISICA', 'QUIMICA',
    'BIOLOGIA', 'MEDICINA', 'SAUDE',
    'ALIMENTACAO', 'EXERCICIO', 'BEMESTAR', 'QUALIDADEDEVIDA', 'LAZER', 'VIAGEM',
    'CULTURA', 'ARTE', 'MUSICA', 'CINEMA',
    'LIVRO', 'JORNAL', 'REVISTA', 'NOTICIA', 'ENTRETENIMENTO', 'ESPORTE', 'FUTEBOL',
    'BASQUETE', 'VOLEIBOL', 'TENIS',
    'NATACAO', 'ATLETISMO', 'CICLISMO', 'CORRIDA', 'GINASTICA', 'YOGA', 'PILATES',
    'MEDITACAO', 'RELAXAMENTO', 'SONO',
    'DESCANSO', 'FERIAS', 'PASSEIO', 'FESTA', 'ANIVERSARIO', 'CASAMENTO', 'FORMATURA',
    'CONFRATERNIZACAO', 'CELEBRACAO', 'PRESENTE',
    'SORRISO', 'FELICIDADE', 'AMOR', 'PAZ', 'ESPERANCA', 'FE', 'GRATIDAO', 'HUMILDADE',
    'RESPEITO', 'TOLERANCIA'
    ];
    const gridSize = 15; // Aumentei para acomodar palavras maiores
    let gameBoard = [];
    let selectedCells = [];
    let foundWords = [];
    let wordsToFind = []; // Inicializa wordsToFind aqui
    const gameBoardElement = document.getElementById('game-board');
    const wordListElement = document.getElementById('words');
    const messageElement = document.getElementById('message');
    // Função para escolher 20 palavras aleatórias
    function chooseRandomWords(wordList, count) {
    const shuffled = [...wordList].sort(() => 0.5 - Math.random());
    return shuffled.slice(0, count);
    }
    // Função para gerar o tabuleiro
    function generateBoard() {
    // Escolhe 20 palavras aleatórias
    wordsToFind = chooseRandomWords(allWords, 20);
    gameBoard = Array.from({ length: gridSize }, () => Array(gridSize).fill(''));
    // Insere as palavras no tabuleiro
    wordsToFind.forEach(word => {
    placeWord(word);
    });
    // Preenche os espaços vazios com letras aleatórias
    for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
    if (gameBoard[i][j] === '') {
    gameBoard[i][j] = String.fromCharCode(65 + Math.floor(Math.random() * 26)); //Letras maiúsculas aleatórias
    }
    }
    }
    }
    // Função para posicionar uma palavra no tabuleiro
    function placeWord(word) {
    let placed = false;
    let attempts = 0; // Adiciona um limite de tentativas
    while (!placed && attempts < 1000) { // Limita as tentativas para evitar loops infinitos
    attempts++;
    const row = Math.floor(Math.random() * gridSize);
    const col = Math.floor(Math.random() * gridSize);
    const direction = Math.floor(Math.random() * 2); // 0: horizontal, 1: vertical
    if (canPlaceWord(word, row, col, direction)) {
    for (let i = 0; i < word.length; i++) {
    if (direction === 0) {
    gameBoard[row][col + i] = word[i];
    } else {
    gameBoard[row + i][col] = word[i];
    }
    }
    placed = true;
    }
    }
    if (!placed) {
    console.warn(`Não foi possível posicionar a palavra "${word}" após várias tentativas.`);
    }
    }
    // Função para verificar se uma palavra pode ser colocada em uma posição
    function canPlaceWord(word, row, col, direction) {
    if (direction === 0 && col + word.length > gridSize) return false;
    if (direction === 1 && row + word.length > gridSize) return false;
    for (let i = 0; i < word.length; i++) {
    if (direction === 0 && gameBoard[row][col + i] !== '' && gameBoard[row][col + i] !==
    word[i]) return false;
    if (direction === 1 && gameBoard[row + i][col] !== '' && gameBoard[row + i][col] !==
    word[i]) return false;
    }
    return true;
    }
    // Função para renderizar o tabuleiro na tela
    function renderBoard() {
    gameBoardElement.innerHTML = '';
    for (let i = 0; i < gridSize; i++) {
    for (let j = 0; j < gridSize; j++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.textContent = gameBoard[i][j];
    cell.dataset.row = i;
    cell.dataset.col = j;
    cell.addEventListener('click', selectCell);
    gameBoardElement.appendChild(cell);
    }
    }
    }
    // Função para renderizar a lista de palavras
    function renderWordList() {
    wordListElement.innerHTML = '';
    wordsToFind.forEach(word => {
    const listItem = document.createElement('li');
    listItem.textContent = word;
    listItem.dataset.word = word;
    wordListElement.appendChild(listItem);
    });
    }
    // Função para selecionar uma célula
    function selectCell(event) {
    const cell = event.target;
    const row = parseInt(cell.dataset.row);
    const col = parseInt(cell.dataset.col);
    // Adiciona ou remove a célula da seleção
    const index = selectedCells.findIndex(c => c.row === row && c.col === col);
    if (index > -1) {
    selectedCells.splice(index, 1);
    cell.classList.remove('selected');
    } else {
    selectedCells.push({ row, col, letter: cell.textContent });
    cell.classList.add('selected');
    }
    // Ordena as células selecionadas para facilitar a verificação
    selectedCells.sort((a, b) => {
    if (a.row !== b.row) return a.row - b.row;
    return a.col - b.col;
    });
    // Verifica se a seleção forma uma palavra
    checkWord();
    }
    // Função para verificar se as células selecionadas formam uma palavra
    function checkWord() {
    const selectedWord = selectedCells.map(cell => cell.letter).join('');
    if (wordsToFind.includes(selectedWord)) {
    markWordAsFound(selectedWord);
    clearSelection();
    checkWin();
    }
    }
    // Função para marcar uma palavra como encontrada
    function markWordAsFound(word) {
    foundWords.push(word);
    // Adiciona a classe 'found-word' à palavra na lista
    const wordListItem = wordListElement.querySelector(`[data-word="${word}"]`);
    wordListItem.classList.add('found-word');
    // Adiciona a classe 'found' às células da palavra no tabuleiro
    selectedCells.forEach(cell => {
    const cellElement = gameBoardElement.querySelector(`[data-row="${cell.row}"][datacol="${cell.col}"]`);
    cellElement.classList.add('found');
    });
    }
    // Função para limpar a seleção
    function clearSelection() {
    selectedCells.forEach(cell => {
    const cellElement = gameBoardElement.querySelector(`[data-row="${cell.row}"][datacol="${cell.col}"]`);
    cellElement.classList.remove('selected');
    });
    selectedCells = [];
    }
    // Função para verificar se o jogador venceu
    function checkWin() {
    if (foundWords.length === wordsToFind.length) {
    messageElement.textContent = 'Parabéns! Você encontrou todas as palavras!';
    }
    }
    // Inicialização do jogo
    function init() {
    generateBoard();
    renderBoard();
    renderWordList();
    }
    init();
    });
