<template>
    <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <router-link class="navbar-brand"  to="/">Home</router-link>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <router-link class="nav-link "  to="/dgr_period">Dgr_period</router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link "  to="/stu_create">Create Stu_Group</router-link>
                </li>
            </ul>
            </div>
        </div>
    </nav>
    </div>
</template>

<script>

    export default{
        name:'nav-bar',
    }
</script>

<!-- <style>
   ul.hr {
    margin: 0; /* Обнуляем значение отступов */
    padding: 4px; /* Значение полей */
   }
   ul.hr li {
    display: inline; /* Отображать как строчный элемент */
    margin-right: 5px; /* Отступ слева */
    padding: 3px; /* Поля вокруг текста */
   }
  </style> -->