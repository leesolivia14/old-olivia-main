
function displayForm(formType){
    const form = document.getElementById(formType);

    console.log(form)
}

function clearAll(){
    const forms = ['locationform', 'budgetform', 'SATreadform', 'SATmathform', 'sizeform', 'ACTform'];
    for (let i=0; i<6; i++) {
        const form = document.getElementById(forms[i]);
        form.style.display = "none";
    }
}

function main(){
    document.addEventListener("click", function(evt) {
        console.log(evt.target.id);

        if (evt.target.id==='locationimg'){
            const form = document.getElementById("locationform");
            console.log(form.style);
            clearAll();
            form.style.display = "block"; 

            const button = document.getElementById("button"); 
            button.style.display = "block";
        }

        else if (evt.target.id==='budgetimg'){
            const form = document.getElementById("budgetform");
            console.log(form.style);
            
            clearAll();

            form.style.display = "block";
            const button = document.getElementById("button"); 
            button.style.display = "block";

        } else if (evt.target.id==='SATreadimg'){
            const form = document.getElementById("SATreadform");
            console.log(form.style);
            
            clearAll();

            form.style.display = "block";
            const button = document.getElementById("button"); 
            button.style.display = "block";

        } else if (evt.target.id==='SATmathimg'){
            const form = document.getElementById("SATmathform");
            console.log(form.style);
            
            clearAll();

            form.style.display = "block";
            const button = document.getElementById("button"); 
            button.style.display = "block";

        }else if (evt.target.id==='ACTimg'){
            const form = document.getElementById("ACTform");
            console.log(form.style);
            
            clearAll();

            form.style.display = "block";

            const button = document.getElementById("button"); 
            button.style.display = "block";

        } else if (evt.target.id==='sizeimg'){
            const form = document.getElementById("sizeform");
            console.log(form.style);
            
            clearAll();

            form.style.display = "block";
            const button = document.getElementById("button"); 
            button.style.display = "block";

        }

    });
}

document.addEventListener('DOMContentLoaded', main);