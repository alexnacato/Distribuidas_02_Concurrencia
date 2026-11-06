import asyncio
import time

# Concurrencia: la cocina de un restaurante prepara varios platos a la vez.
# Mientras un plato se cocina, el cocinero avanza con los demás.


async def preparar_plato(nombre, segundos):
    print(f"Empieza: {nombre}")
    await asyncio.sleep(segundos)  # Simula el tiempo de preparación
    print(f"Listo: {nombre} ({segundos} s)")


async def main():
    print("=== Cocina del restaurante ===\n")

    inicio = time.perf_counter()

    # gather inicia todos los platos al mismo tiempo
    await asyncio.gather(
        preparar_plato("Pizza", 4),
        preparar_plato("Hamburguesa", 3),
        preparar_plato("Sopa", 2),
        preparar_plato("Ensalada", 1),
    )

    fin = time.perf_counter()

    print(f"\nTiempo total: {fin - inicio:.2f} segundos.")
    print("De forma secuencial habría tardado 10 segundos.")


asyncio.run(main())
