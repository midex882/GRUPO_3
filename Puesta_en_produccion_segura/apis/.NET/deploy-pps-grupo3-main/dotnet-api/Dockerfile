# -------------------------------
# Stage 1: Build
# -------------------------------
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copiar archivos del proyecto y restaurar dependencias
COPY dotnet-api.csproj ./
RUN dotnet restore

# Copiar todo el código fuente y compilar
COPY . .
RUN dotnet publish -c Release -o /app/publish

# -------------------------------
# Stage 2: Runtime
# -------------------------------
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS runtime
WORKDIR /app

# Copiar los binarios publicados
COPY --from=build /app/publish ./

# Copiar el archivo de datos
COPY data.json .

# Exponer el puerto 8001
EXPOSE 8001

# Establecer el punto de entrada
ENTRYPOINT ["dotnet", "dotnet-api.dll", "--urls", "http://0.0.0.0:8001"]
