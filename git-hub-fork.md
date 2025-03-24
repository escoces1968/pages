# 🚀 Guía Completa para Trabajar con un Fork en GitHub  

## 📌 1. Hacer el Fork y Clonarlo  
Cuando haces un **fork**, GitHub crea una copia del repositorio en tu cuenta. Ahora necesitas clonar ese fork en tu máquina local.  

1. **Haz el fork** en GitHub (botón "Fork" en la esquina superior derecha).  
2. **Clona el fork** en tu computadora:  
   ```sh
   git clone https://github.com/tu-usuario/mi-repo.git
   cd mi-repo
   ```
3. **Verifica los remotos**:  
   ```sh
   git remote -v
   ```
   Esto debe mostrar:  
   ```
   origin    https://github.com/tu-usuario/mi-repo.git (fetch)
   origin    https://github.com/tu-usuario/mi-repo.git (push)
   ```

---

## 🔗 2. Conectar con el Repositorio Original (Upstream)  
Para mantener tu fork actualizado con los cambios del repo original, agrega un **remoto adicional (`upstream`)**.  

```sh
git remote add upstream https://github.com/usuario-original/mi-repo.git
```
Verifica que se agregó correctamente:  
```sh
git remote -v
```
Ahora deberías ver:  
```
origin    https://github.com/tu-usuario/mi-repo.git (fetch)
origin    https://github.com/tu-usuario/mi-repo.git (push)
upstream  https://github.com/usuario-original/mi-repo.git (fetch)
upstream  https://github.com/usuario-original/mi-repo.git (push)
```

---

## 🔄 3. Mantener tu Fork Actualizado
Cada vez que el repositorio original reciba cambios, debes traerlos a tu fork para mantenerlo al día.

1. **Descargar cambios del repositorio original**:
   ```sh
   git fetch upstream
   ```
2. **Fusionar los cambios en tu rama `main`**:
   ```sh
   git checkout main
   git merge upstream/main
   ```
   *(Si prefieres reescribir el historial en lugar de hacer un merge, usa `git rebase upstream/main` en lugar de `merge`.)*
3. **Subir los cambios a tu fork en GitHub**:
   ```sh
   git push origin main
   ```

---

## 🌿 4. Crear una Rama Nueva para Trabajar  
Nunca trabajes directamente en `main`. Es mejor crear una rama para cada cambio.  

1. **Crea una nueva rama** basada en `main`:  
   ```sh
   git checkout -b mi-nueva-rama
   ```
2. **Haz cambios en tu código** y agrégalos al commit:  
   ```sh
   git add .
   git commit -m "Descripción de mis cambios"
   ```
3. **Sube la nueva rama a tu fork**:  
   ```sh
   git push origin mi-nueva-rama
   ```

---

## 🔁 5. Hacer un Pull Request (PR)  
Cuando termines los cambios y quieras que se integren en el repo original, haz un **Pull Request**.  

1. Ve a **GitHub → Tu Fork**.  
2. Verás un botón que dice **"Compare & pull request"**, haz clic.  
3. Asegúrate de que la base es **`usuario-original/main`** y la comparación es **`tu-usuario/mi-nueva-rama`**.  
4. Escribe una descripción clara de los cambios.  
5. Haz clic en **"Create Pull Request"**.  

El dueño del repo original revisará tu PR y podrá fusionarlo. 🚀  

---

## 🔄 6. Mantener tu Rama Actualizada  
Si el repositorio original tiene cambios mientras trabajas en tu rama, debes actualizarla para evitar conflictos.  

1. **Traer los cambios del repo original**:  
   ```sh
   git fetch upstream
   ```
2. **Actualizar tu rama con los últimos cambios de `main`**:  
   ```sh
   git checkout mi-nueva-rama
   git merge upstream/main
   ```
   *(O si prefieres reescribir el historial:)*  
   ```sh
   git rebase upstream/main
   ```
3. **Subir los cambios actualizados a tu fork**:  
   ```sh
   git push origin mi-nueva-rama
   ```

---

## 🔥 7. Cambiar Entre la `main` del Fork y la del Repo Original  
Si necesitas ver la `main` del repo original sin afectar tu fork:

1. **Ver tu `main` (fork):**  
   ```sh
   git checkout main
   ```
   Si `main` está mal configurado y apunta al repo original en lugar de tu fork, corrígelo:  
   ```sh
   git branch --set-upstream-to=origin/main main
   ```

2. **Ver la `main` del repo original sin modificar nada:**  
   ```sh
   git fetch upstream
   git checkout -b upstream-main upstream/main
   ```
   Esto crea una nueva rama `upstream-main` basada en la `main` del repo original.

---

## 🚨 8. Forzar que `main` Sea Igual a `upstream/main`  
Si tu fork está desactualizado y quieres que tu `main` sea idéntico al repo original:  

```sh
git checkout main
git fetch upstream
git reset --hard upstream/main
git push origin main --force
```
⚠️ **Cuidado:** `reset --hard` borra cualquier cambio local en `main`.

---

## 📌 Resumen Final  
1. **Clona tu fork y configura `upstream`**.  
2. **Mantén tu fork actualizado** con `git fetch upstream` + `git merge upstream/main`.  
3. **Crea una nueva rama para cada cambio** antes de modificar código.  
4. **Haz commits y sube la rama a tu fork** con `git push origin mi-nueva-rama`.  
5. **Abre un Pull Request** en GitHub para contribuir al repo original.  
6. **Si el repo original cambia, actualiza tu rama** con `git fetch upstream` + `git merge upstream/main`.  

---

¡Y listo! Ahora tienes todo lo que necesitas para trabajar con forks y contribuir a repositorios de código abierto como un pro. 🚀😎
