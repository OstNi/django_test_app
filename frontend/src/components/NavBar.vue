<template>
    <nav class="navbar navbar-expand-lg bg-light">
        <div class="container">
            <div class="collapse navbar-collapse" id="navbarText">
                <ul class="hr">
                    <li class="nav-item">
                        <router-link class="nav-link "  to="/">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link "  to="/dgr_period">Dgr_period</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link "  to="/tw_block">Tw_block</router-link>
                    </li>
                </ul>
                <span class="navbar-text">
                </span>
            </div>
        </div>
    </nav>
</template>

<script>
    export default{
        name:'nav-bar'
    }
</script>

<style>
   ul.hr {
    margin: 0; /* Обнуляем значение отступов */
    padding: 4px; /* Значение полей */
   }
   ul.hr li {
    display: inline; /* Отображать как строчный элемент */
    margin-right: 5px; /* Отступ слева */
    padding: 3px; /* Поля вокруг текста */
   }
  </style>