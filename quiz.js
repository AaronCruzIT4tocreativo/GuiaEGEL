let currentQuestionIndex = 0;
let questions = [];

// Función para cargar los archivos JSON
async function fetchQuestion(index) {
    try {
        const response = await fetch(`./sorted_answers/salida_${index}.json`);
        if (!response.ok) {
            throw new Error(`No se pudo cargar el archivo salida_${index}.json`);
        }
        const questionData = await response.json();

        console.log(`Contenido de salida_${index}.json:`, questionData);

        // Verificación de la estructura correcta
        if (Array.isArray(questionData) && questionData.length > 0) {
            questionData.forEach((question) => {
                if (question.imageName && question.imageIndex && question.index !== undefined && question.text && Array.isArray(question.options) && question.options.length > 0 && question.answer) {
                    questions.push(question);
                } else {
                    console.warn(`El archivo salida_${index}.json tiene una estructura incorrecta para la pregunta ${question.index}`);
                }
            });
        } else {
            console.warn(`El archivo salida_${index}.json no contiene datos válidos.`);
        }
    } catch (error) {
        console.error("Error al cargar el archivo:", `salida_${index}.json`, error);
    }
}

// Función para cargar todas las preguntas
async function loadQuestions() {
    const totalFiles = 11; // Ajusta este número según la cantidad de archivos disponibles
    for (let i = 1; i <= totalFiles; i++) {
        await fetchQuestion(i);
    }
    displayQuestion(currentQuestionIndex);
}

// Función para mostrar la pregunta en la interfaz
function displayQuestion(index) {
    const question = questions[index];

    const questionContainer = document.getElementById('question-container');
    questionContainer.innerHTML = ''; // Limpiar la pregunta actual

    // Mostrar el índice de la pregunta
    const questionIndexText = document.createElement('h2');
    questionIndexText.textContent = `Pregunta ${index + 1}`;
    questionContainer.appendChild(questionIndexText);

    // Mostrar el texto de la pregunta
    const questionText = document.createElement('p');
    questionText.classList.add('question-text');
    questionText.textContent = question.text;
    questionContainer.appendChild(questionText);

    // Crear elementos HTML para las opciones
    const optionsContainer = document.createElement('div');
    optionsContainer.classList.add('options');
    question.options.forEach((option, i) => {
        const optionLabel = document.createElement('label');
        const optionInput = document.createElement('input');
        optionInput.type = 'radio';
        optionInput.name = `question-${index}`;
        optionInput.value = i;
        optionInput.classList.add('option');

        optionLabel.appendChild(optionInput);
        optionLabel.appendChild(document.createTextNode(option.text));
        optionsContainer.appendChild(optionLabel);
    });
    questionContainer.appendChild(optionsContainer);

    // Crear el contenedor de explicación
    const explanationContainer = document.createElement('div');
    explanationContainer.classList.add('explanation');
    explanationContainer.id = `explanation-${index}`;
    explanationContainer.style.display = 'none'; // Inicialmente oculto
    const explanationText = document.createElement('p');
    explanationText.textContent = `Explicación: ${question.answer.explanation}`;
    explanationContainer.appendChild(explanationText);
    questionContainer.appendChild(explanationContainer);

    // Mostrar el botón "Siguiente pregunta"
    const nextButton = document.createElement('button');
    nextButton.textContent = "Siguiente pregunta";
    nextButton.id = 'next-question';
    nextButton.style.display = 'none'; // Inicialmente oculto
    nextButton.addEventListener('click', nextQuestion);
    questionContainer.appendChild(nextButton);
}

// Función para manejar la respuesta seleccionada
function checkAnswer() {
    const selectedOption = document.querySelector(`input[name="question-${currentQuestionIndex}"]:checked`);
    const resultContainer = document.getElementById('result');
    
    if (selectedOption) {
        const selectedAnswerIndex = parseInt(selectedOption.value);
        const correctAnswer = questions[currentQuestionIndex].answer.index;

        // Mostrar la explicación
        const explanationContainer = document.getElementById(`explanation-${currentQuestionIndex}`);
        explanationContainer.style.display = 'block'; // Mostrar la explicación

        // Mostrar la respuesta correcta y la explicación
        if (selectedAnswerIndex === correctAnswer) {
            resultContainer.innerHTML = `<span class="correct">¡Respuesta correcta!</span>`;
        } else {
            resultContainer.innerHTML = `
                <span class="incorrect">Respuesta incorrecta.</span>
                <p><strong>Respuesta correcta:</strong> ${questions[currentQuestionIndex].answer.text}</p>
                <p><strong>Explicación:</strong> ${questions[currentQuestionIndex].answer.explanation}</p>
            `;
        }

        // Ocultar los botones de opción y mostrar el botón "Siguiente pregunta"
        const optionsContainer = document.querySelector('.options');
        const nextButton = document.getElementById('next-question');
        nextButton.style.display = 'inline'; // Mostrar el botón de siguiente pregunta
    } else {
        resultContainer.innerHTML = `<span class="incorrect">Por favor, selecciona una respuesta.</span>`;
    }
}

// Función para cambiar a la siguiente pregunta
function nextQuestion() {
    if (currentQuestionIndex < questions.length - 1) {
        currentQuestionIndex++;
        displayQuestion(currentQuestionIndex);
        const resultContainer = document.getElementById('result');
        resultContainer.innerHTML = ''; // Limpiar el resultado
    } else {
        const resultContainer = document.getElementById('result');
        resultContainer.innerHTML = `<span class="correct">¡Has completado el cuestionario!</span>`;
    }
}

// Iniciar el cuestionario al cargar la página
loadQuestions();

// Agregar evento para el botón "Siguiente pregunta"
document.getElementById('next-question').addEventListener('click', checkAnswer);
