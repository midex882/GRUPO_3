<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ItemController extends Controller
{
    private $file = 'data.json';

    private function readData()
    {
        return json_decode(file_get_contents(base_path($this->file)), true);
    }

    private function writeData($data)
    {
        file_put_contents(base_path($this->file), json_encode($data, JSON_PRETTY_PRINT));
    }

    public function index()
    {
        return response()->json($this->readData());
    }

    public function show($id)
    {
        $items = $this->readData();
        $item = collect($items)->firstWhere('id', (int) $id);
        if (!$item) return response()->json(['message' => 'Item not found'], 404);
        return response()->json($item);
    }

    public function store(Request $request)
    {
        $items = $this->readData();
        $item = $request->all();
        $item['id'] = count($items) ? max(array_column($items, 'id')) + 1 : 1;
        $items[] = $item;
        $this->writeData($items);
        return response()->json($item, 201);
    }

    public function update(Request $request, $id)
    {
        $items = $this->readData();
        $index = collect($items)->search(fn($i) => $i['id'] == (int)$id);
        if ($index === false) return response()->json(['message' => 'Item not found'], 404);
        $items[$index] = array_merge($items[$index], $request->all());
        $this->writeData($items);
        return response()->json($items[$index]);
    }

    public function destroy($id)
    {
        $items = $this->readData();
        $index = collect($items)->search(fn($i) => $i['id'] == (int)$id);
        if ($index === false) return response()->json(['message' => 'Item not found'], 404);
        array_splice($items, $index, 1);
        $this->writeData($items);
        return response()->json(null, 204);
    }
}
