
function displayForm(formType){
    const form = document.getElementById(formType);

    console.log(form)
}

function clearAll(){
    const forms = ['locationform', 'budgetform', 'SATform', 'sizeform', 'ACTform'];
    for (let i=0; i<5; i++) {
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
        }

        else if (evt.target.id==='budgetimg'){
            const form = document.getElementById("budgetform");
            console.log(form.style);
            
            clearAll();

            form.style.display = "block";
        } else if (evt.target.id==='SATimg'){
            const form = document.getElementById("SATform");
            console.log(form.style);
            
            clearAll();

            form.style.display = "block";
        } else if (evt.target.id==='placeholder'){
            const form = document.getElementById("placeholderform");
            console.log(form.style);
            
            clearAll();

            form.style.display = "block";
        } else if (evt.target.id==='sizeimg'){
            const form = document.getElementById("sizeform");
            console.log(form.style);
            
            clearAll();

            form.style.display = "block";
        }

    });
    //displayDropdown(formType);
}

document.addEventListener('DOMContentLoaded', main);