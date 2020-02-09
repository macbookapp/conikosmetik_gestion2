
 var nv = new Vue({
            el: '#app',
            data: {

                ingreso: 0,
                gasto: 0,
                total: 0,

            },
            computed: {
                setTotal() {

                    entrada = parseFloat(this.ingreso)
                    salida = parseFloat(this.gasto)
                    total = parseFloat(this.total)

                    console.log('Total = ' + total)

                    total = this.ingreso - this.gasto
                    this.total = total


                    return total


                }
            }
        })
