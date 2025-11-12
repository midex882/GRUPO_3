<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ItemController extends Controller
{
    // File name that contains data for the simple api.
    private $file = 'data.json';

    /**
     *
     */
    private function readData()
    {
        $path = base_path($this->file);
        return json_decode(file_get_contents($path), true);
    }

    /**
     *
     */
    private function writeData($data)
    {
        $path = base_path($this->file);
        file_put_contents($path, json_encode($data, JSON_PRETTY_PRINT));
    }

    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return response()->json($this->readData());
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $items = $this->readData();

        $newItem = $request->only(['nombre', 'precio']);
        $newItem['id'] = count($items) ? max(array_column($items, 'id')) + 1 : 1;

        $items[] = $newItem;
        $this->writeData($items);

        return response()->json($newItem, 201);
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        $items = $this->readData();
        $item = collect($items)->firstWhere('id', (int)$id);

        if (!$item) {
            return response()->json(['error' => 'No encontrado'], 404);
        }

        return response()->json($item);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        $items = $this->readData();
        $index = array_search((int)$id, array_column($items, 'id'));

        if ($index === false) {
            return response()->json(['error' => 'No encontrado'], 404);
        }

        // Actualiza sólo las claves que nos interesan
        $items[$index] = array_merge(
            $items[$index],
            $request->only(['nombre', 'precio'])
        );

        $this->writeData($items);

        return response()->json($items[$index]);
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        $items = $this->readData();
        $items = array_values(array_filter($items, fn($i) => $i['id'] != (int)$id));

        $this->writeData($items);

        return response()->json(['message' => 'Eliminado correctamente']);
    }
}
