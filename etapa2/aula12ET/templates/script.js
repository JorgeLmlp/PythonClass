const elemento = document.getElementById("typing");
const body = document.body
let codigo
if (body.classList.contains("EN")) {
    codigo = [
        { texto: "class Profile:", html: `<span class="keyword">class</span> Profile:` },
        { texto: '    user = "JorgeLmlp"', html: `    <span class="variable">user</span> = <span class="string">"JorgeLmlp"</span>` },
        
        { texto: '    desc = "creating new and affordable solutions for web, mobile development and data science"]', html: `    <span class="variable">desc</span> = <span class="string">"creating new and affordable solutions for web, mobile development and data science"</span>` },

        { texto: '    Programming_languages = ["Python", "javascript", "HTML", "CSS", "Swift", "Kotlin", "Flutter"]', html: `    <span class="variable">Programming languages</span> = <span class = "colchetes">[</span> <span class="string">"Python","javascript", "HTML, CSS, "Swift", "Kotlin", "Flutter" </span> <span class = "colchetes">]</span>` },
        { texto: '    tools = ["Flask", "React", "vite", "Tailwindcss", "Pandas"]', html: `    <span class="variable">tools</span> = <span class="string">"Flask", "React","Vite","Pandas","Tailwindcss"</span> <span class = "colchetes">]</span> ` },


        { texto: "def hello_world():", html: `<span class="keyword">def</span> <span class="function">Hello_world</span>():` },

        { texto: '   print("Hello world")', html: `    print(<span class="string">"Hello world"</span>)` },

        { texto: "hello_world()", html: `<span class="function">Hello_world</span>()` }
    ];
}
else {
    codigo = [
        { texto: "class Nome:", html: `<span class="keyword">class</span> Nome:` },

        { texto: '    usuario = "JorgeLmlp"', html: `    <span class="variable">usuario</span> = <span class="string">"JorgeLmlp"</span>` },

        { texto: '    descricao = "criando soluções novas e acessíveis para desenvolvimento web, mobile e ciência de dados"', html: `    <span class="variable">descricao</span> = <span class="string">"criando soluções novas e acessíveis para desenvolvimento web, mobile e ciência de dados"</span>` },

        { texto: '    linguagens_de_programacao = ["Python", "JavaScript", "HTML", "CSS", "Swift", "Kotlin", "Flutter"]', html: `    <span class="variable">linguagens_de_programacao</span> = [<span class="string">"Python"</span>, <span class="string">"JavaScript"</span>, <span class="string">"HTML"</span>, <span class="string">"CSS"</span>, <span class="string">"Swift"</span>, <span class="string">"Kotlin"</span>, <span class="string">"Flutter"</span>]` },

        { texto: '    ferramentas = ["Flask", "React", "Vite", "TailwindCSS", "Pandas"]', html: `    <span class="variable">ferramentas</span> = [<span class="string">"Flask"</span>, <span class="string">"React"</span>, <span class="string">"Vite"</span>, <span class="string">"TailwindCSS"</span>, <span class="string">"Pandas"</span>]` },

        { texto: "def ola_mundo():", html: `<span class="keyword">def</span> <span class="function">ola_mundo</span>():` },

        { texto: '   print("Olá mundo")', html: `    print(<span class="string">"Olá mundo"</span>)` },

        { texto: "hello world()", html: `<span class="function">hello world</span>()` }
    ]
}
let linha = 0;
let char = 0;

function digitar() {
    if (linha < codigo.length) {


        let linhas = elemento.querySelectorAll(".linha");

        if (!linhas[linha]) {
            const novaLinha = document.createElement("div");
            novaLinha.classList.add("linha");
            elemento.appendChild(novaLinha);
        }

        const linhaAtual = elemento.querySelectorAll(".linha")[linha];

        if (char < codigo[linha].texto.length) {
            linhaAtual.textContent += codigo[linha].texto.charAt(char);
            char++;
            setTimeout(digitar, 20);
        } else {
            linhaAtual.innerHTML = codigo[linha].html;

            linha++;
            char = 0;
            setTimeout(digitar, 200);
        }
    }
}

digitar();

const temaSalvo = localStorage.getItem("tema")
const light = document.getElementById("light")

body.classList.toggle("light", localStorage.getItem("tema") === "light");

light.addEventListener("click", () => {
    const isLight = body.classList.toggle("light");
    localStorage.setItem("tema", isLight ? "light" : "dark");
});