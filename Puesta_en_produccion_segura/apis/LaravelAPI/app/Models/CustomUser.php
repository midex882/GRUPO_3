<?php

namespace App\Models;

use Illuminate\Contracts\Auth\Authenticatable;
use Tymon\JWTAuth\Contracts\JWTSubject;

class CustomUser implements Authenticatable, JWTSubject
{
    protected $attributes;

    public function __construct(array $attributes)
    {
        $this->attributes = $attributes;
    }

    public function getAuthIdentifierName()
    {
        return 'id';
    }

    public function getAuthIdentifier()
    {
        return $this->attributes['id'];
    }

    public function getAuthPassword()
    {
        return null; // Not using hashed passwords
    }

    public function getRememberToken()
    {
        return null;
    }

    public function setRememberToken($value)
    {
        // Not needed
    }

    public function getRememberTokenName()
    {
        return null;
    }

    public function getAuthPasswordName()
    {
        return 'password';
    }

    // JWT Methods
    public function getJWTIdentifier()
    {
        return $this->attributes['id'];
    }

    public function getJWTCustomClaims()
    {
        return [];
    }

    // Helper to get attributes
    public function __get($key)
    {
        return $this->attributes[$key] ?? null;
    }
}
