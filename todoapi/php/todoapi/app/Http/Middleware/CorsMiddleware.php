<?php 
    namespace App\Http\Middleware;

    use Closure;

    class CorsMiddleware 
    {
        /**
         * Handle an incoming request.
         *
         * @param  \Illuminate\Http\Request  $request
         * @param  \Closure  $next
         * @return mixed
         */
        public function handle($request, Closure $next)
        {
            $headers = [
                'Access-Control-Allow-Origin'      => '*',
                'Access-Control-Allow-Methods'     => 'HEAD, GET, POST, PUT, PATCH, DELETE, OPTIONS',
                'Access-Control-Allow-Credentials' => 'true',
                'Access-Control-Max-Age'           => '86400',
                'Access-Control-Allow-Headers'     => $request->header('Access-Control-Request-Headers'),
                'Access-Control-Expose-Headers'    => 'Location'
            ];

            if ($request->isMethod('OPTIONS'))
            {
                return response()->json('', 204, $headers);
            }

            $response = $next($request);
            foreach($headers as $key => $value)
            {
                $response->header($key, $value);
            }

            return $response;
        }
    }
